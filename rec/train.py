import os
import torch
import cv2
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
import model as crnn
import time


# 调整图像大小和归一化操作
class resizeAndNormalize():
    def __init__(self, size, interpolation=cv2.INTER_LINEAR):
        # 注意对于opencv,size的格式是(w,h)
        self.size = size
        self.interpolation = interpolation
        # ToTensor属于类  """Convert a ``PIL Image`` or ``numpy.ndarray`` to tensor.
        self.toTensor = transforms.ToTensor()

    def __call__(self, image):
        # (x,y) 对于opencv来说，图像宽对应x轴，高对应y轴
        image = cv2.resize(image, self.size, interpolation=self.interpolation)
        # 转为tensor的数据结构
        image = self.toTensor(image)
        # 对图像进行归一化操作
        image = image.sub_(0.5).div_(0.5)
        return image


class CRNNDataSet(Dataset):
    def __init__(self, imageRoot, labelRoot):
        self.image_root = imageRoot
        self.image_dict = self.readfile(labelRoot)
        self.image_name = [fileName for fileName, _ in self.image_dict.items()]

    def __getitem__(self, index):
        image_path = os.path.join(self.image_root, self.image_name[index])
        keys = self.image_dict.get(self.image_name[index])
        label = [int(x) for x in keys]  # TODO 还没搞明白data.txt是怎么表示的

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # if image is None:
        #     return None,None
        (height, width) = image.shape

        # 由于crnn网络输入图像的高为32，故需要resize原始图像的height
        size_height = 32
        ratio = 32/float(height)
        size_width = int(ratio * width)
        transform = resizeAndNormalize((size_width, size_height))
        # 图像预处理
        image = transform(image)
        # 标签格式转换为IntTensor
        label = torch.IntTensor(label)

        return image, label

    def __len__(self):
        return len(self.image_name)

    def readfile(self, fileName):
        res = []
        with open(fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                res.append(line.strip())
        dic = {}
        total = 0
        for line in res:
            part = line.split(' ')
            # 由于会存在训练过程中取图像的时候图像不存在导致异常，所以在初始化的时候就判断图像是否存在
            if not os.path.exists(os.path.join(self.image_root, part[0])):
                print(os.path.join(self.image_root, part[0]))
                total += 1
            else:
                dic[part[0]] = part[1:]
        print(total)

        return dic

current_work_dir = os.path.dirname(__file__)
trainData = CRNNDataSet(imageRoot=current_work_dir+"/data/images",
                        labelRoot=current_work_dir+"/data/labels/data.txt")

trainLoader = DataLoader(
    dataset=trainData, batch_size=30, shuffle=True, num_workers=0)

valData = CRNNDataSet(imageRoot=current_work_dir+"/data/images",
                      labelRoot=current_work_dir+"/data/labels/data.txt")

valLoader = DataLoader(dataset=valData, batch_size=1,
                       shuffle=True, num_workers=1)


def decode(preds):
    pred = []
    for i in range(len(preds)):
        if preds[i] != 5989 and ((i == 5989) or (i != 5989 and preds[i] != preds[i-1])):
            pred.append(int(preds[i]))
    return pred


def val(model, loss_function, max_iteration, use_gpu=False):
    # 将模式切换为验证评估模式
    model.eval()
    k = 0
    totalloss = 0
    correct_num = 0
    total_num = 0
    val_iter = iter(valLoader)
    max_iter = min(max_iteration, len(valLoader))

    for i in range(max_iter):
        k = k + 1
        data, label = val_iter.next()
        labels = torch.IntTensor([])
        for j in range(label.size(0)):
            labels = torch.cat((labels, label[j]), 0)

        if torch.cuda.is_available() and use_gpu:
            data = data.cuda()
        output = model(data)
        input_lengths = torch.IntTensor([output.size(0)] * int(output.size(1)))
        target_lengths = torch.IntTensor([label.size(1)] * int(label.size(0)))
        loss = loss_function(output, labels, input_lengths,
                             target_lengths) / label.size(0)
        totalloss += float(loss)
        pred_label = output.max(2)[1]
        pred_label = pred_label.transpose(1, 0).contiguous().view(-1)
        pred = decode(pred_label)
        total_num += len(pred)
        for x, y in zip(pred, labels):
            if int(x) == int(y):
                correct_num += 1
    accuracy = correct_num / float(total_num) * 100
    test_loss = totalloss / k
    print('Test loss : %.3f , accuary : %.3f%%' % (test_loss, accuracy))


def train():
    use_gpu = False
    learning_rate = 0.0005
    weight_decay = 1e-4
    max_epoch = 10
    current_work_dir = os.path.dirname(__file__)
    modelpath = current_work_dir+"/model/model.pth"
    char_set = open(current_work_dir+'/data/char.txt',
                    'r', encoding='utf-8').readlines()
    char_set = ''.join([ch.strip('\n') for ch in char_set[1:]] + ['卍'])
    n_class = len(char_set)

    model = crnn.CRNN(imgHeight=32, nChannel=1, nClass=n_class, nHidden=256)
    if torch.cuda.is_available() and use_gpu:
        model.cuda()

    loss_func = torch.nn.CTCLoss(blank=n_class-1)
    optimizer = torch.optim.Adam(
        model.parameters(), lr=learning_rate, weight_decay=weight_decay)

    if os.path.exists(modelpath):
        print("load model from %s" % modelpath)
        model.load_state_dict(torch.load(modelpath))
        print("done!")

    lossTotal = 0.0
    k = 0
    printInterval = 100
    valinterval = 1000
    start_time = time.time()
    for epoch in range(max_epoch):

        for i, (data, label) in enumerate(trainLoader):

            k = k + 1
            # 开启训练模式
            model.train()

            labels = torch.IntTensor([])
            for j in range(label.size(0)):
                labels = torch.cat((labels, label[j]), 0)

            if torch.cuda.is_available and use_gpu:
                data = data.cuda()
                loss_func = loss_func.cuda()
                labels = labels.cuda()

            output = model(data)

            # log_probs = output
            # example 建议使用这样，貌似直接把output送进去loss fun也没发现什么问题
            log_probs = output.log_softmax(2).detach().requires_grad_()
            targets = labels
            input_lengths = torch.IntTensor(
                [output.size(0)] * int(output.size(1)))
            target_lengths = torch.IntTensor(
                [label.size(1)] * int(label.size(0)))

            # forward(self, log_probs, targets, input_lengths, target_lengths)
            loss = loss_func(log_probs, targets, input_lengths,
                            target_lengths) / label.size(0)
            lossTotal += float(loss)

            if k % printInterval == 0:

                print("[%d/%d] [%d/%d] loss:%f" % (
                    epoch, max_epoch, i + 1, len(trainLoader), lossTotal/printInterval))
                lossTotal = 0.0
                current_work_dir = os.path.dirname(__file__)
                torch.save(model.state_dict(),
                        current_work_dir+"/model/model.pth")

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if k % valinterval == 0:
                val(model, loss_func)

    end_time = time.time()
    print("takes {}s".format((end_time - start_time)))


if __name__ == '__main__':
    train()
