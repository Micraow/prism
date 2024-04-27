# 以下内容为接口规范，务必实现，除此之外还可另外创建类或方法，只要要求的接口能正常工作
# 建议其他方法在另外的文件里写再import进来，保持有序
import cv2
import os
import enhancer

current_file_dir = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(current_file_dir, ".."))
gallery_dir = os.path.join(root,"/web/front/prism-web/src/assets/gallery/")

def get_index(dir=gallery_dir):
    file_list = os.listdir(dir) # 按字典顺序从小到大排的
    for i in file_list.reverse():
        if i[-4:] == ".jpg":
            index = i[:-4]
    return index + 1

class cv():
    def __init__(self):
        if os.path.exists("/tmp/prism") is not True:
            os.mkdir("/tmp/prism")
        self.cap = cv2.VideoCapture(0)  # 参数为0时调用本地摄像头；参数为1时调用外接摄像头
        self.index = get_index()
        self.stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
        # print("初始化的工作（如果有）")

    def takePic(self):
        ret, frame = self.cap.read()  # ret(bool)有无读取到图片
        cv2.imwrite("/tmp/prism/"+str(self.index)+".jpg", frame)
        path = "/tmp/prism/"+str(self.index)+".jpg"
        self.index = self.index + 1
        self.cap.release()
        self.cap = cv2.VideoCapture(0)
        return path

    # def startCapture(self, wait_time):
    #     # 间隔固定时间（wait_time)(毫秒) 拍照，获得一系列图片，用于合成,直到stopCapture被调用

    # def stopCapture(self):
    #     images_paths = []
    #     return images_paths

    def stitch(self, images_paths):
        # images_paths是一系列要拼接的图片的路径构成的列表
        # 参考：https://www.geeksforgeeks.org/opencv-panorama-stitching
        imgs = []
        for image_path in images_paths:
            img = cv2.imread(image_path)
            imgs.append(img)
        (ret, pano) = self.stitcher.stitch(imgs)
        path = "/tmp/prism/"+str(self.index)+".jpg"
        cv2.imwrite(path, pano)
        self.index = self.index+1
        return path

    def enhance(self, image_path):
        # 传入全景拼接后或保存的版书/错题图片，返回增强（类似扫描全能王）后的图片路径(灰度图片)
        # 参考：https://www.cnblogs.com/skyfsm/p/7324346.html
        res = enhancer.enhance(image_path)
        path = "/tmp/prism/"+str(self.index)+".jpg"
        cv2.imwrite(path, res)
        self.index = self.index+1
        return path

    def clean(self, path="/tmp/prism"):
        # 清理保存的一系列图片，无返回值
        ls = os.listdir(path)
        for i in ls:
            f_path = os.path.join(path, i)
        # 判断是否是一个目录,若是,则递归删除
            if os.path.isdir(f_path):
                self.clean(f_path)
            else:
                os.remove(f_path)

    def save(self, img):
        path = gallery_dir + str(self.index) + ".jpg"
        cv2.imwrite(path, img)
        self.index = self.index + 1
        return path
