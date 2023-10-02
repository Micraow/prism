import os

import torch

import model as crnn
from PIL import Image
from torchvision import transforms


class resizeNormalize(object):
    def __init__(self, size, interpolation=Image.BILINEAR):
        self.size = size
        self.interpolation = interpolation
        self.toTensor = transforms.ToTensor()

    def __call__(self, img):
        img = img.resize(self.size, self.interpolation)
        img = self.toTensor(img)
        img.sub_(0.5).div_(0.5)
        return img


def decode(preds, char_set):
    pred_text = ''
    for i in range(len(preds)):
        if preds[i] != 5989 and ((i == 5989) or (i != 5989 and preds[i] != preds[i-1])):
            pred_text += char_set[int(preds[i])-1]

    return pred_text

# test if crnn work


if __name__ == '__main__':

    imagepath = './input.jpg'

    img_h = input("img_h?")
    use_gpu = False
    current_work_dir = os.path.dirname(__file__)
    modelpath = current_work_dir+"/model/model.pth"
    char_set = open(current_work_dir+'/data/char.txt',
                    'r', encoding='utf-8').readlines()
    char_set = ''.join([ch.strip('\n') for ch in char_set[1:]] + ['卍'])
    n_class = len(char_set)
    print(n_class)

    from model import crnn
    model = crnn.CRNN(img_h, 1, n_class, 256)

    if os.path.exists(modelpath):
        print('Load model from "%s" ...' % modelpath)
        model.load_state_dict(torch.load(modelpath))
        print('Done!')

    if torch.cuda.is_available and use_gpu:
        model.cuda()

    image = Image.open(imagepath).convert('L')
    (w, h) = image.size
    size_h = 32
    ratio = size_h / float(h)
    size_w = int(w * ratio)
    # keep the ratio
    transform = resizeNormalize((size_w, size_h))
    image = transform(image)
    image = image.unsqueeze(0)
    if torch.cuda.is_available and use_gpu:
        image = image.cuda()
    model.eval()
    preds = model(image)
    preds = preds.max(2)
    preds = preds[1]
    preds = preds.squeeze()
    pred_text = decode(preds, char_set)
    print('predict == >', pred_text)
