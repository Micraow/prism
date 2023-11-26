# 以下内容为接口规范，务必实现，除此之外还可另外创建类或方法，只要要求的接口能正常工作
# 建议其他方法在另外的文件里写再import进来，保持有序
class cv():
    def __init__(self):
        print("初始化的工作（如果有）")

    def takePic(self):
        path = "/path/to/image"
        return path

    def startCapture(self, wait_time):
        # 间隔固定时间（wait_time)(毫秒) 拍照，获得一系列图片，用于合成,直到stopCapture被调用
        pass

    def stopCapture(self):
        images_paths=[]
        return images_paths

    def stitch(self, images_paths):
        # images_paths是一系列要拼接的图片的路径构成的列表
        # 参考：https://www.geeksforgeeks.org/opencv-panorama-stitching
        path = "final image path"
        return path

    def enhance(self, image_path):
        # 传入全景拼接后或保存的版书/错题图片，返回增强（类似扫描全能王）后的图片路径(灰度图片)
        # 参考：https://www.cnblogs.com/skyfsm/p/7324346.html
        path = "final image path"
        return path

    def clean(self):
        # 清理保存的一系列图片，无返回值
        pass
