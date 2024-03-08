from paddleocr import PaddleOCR

# 安装PaddleOCR的指令，使用whl版以确保包名正确
# pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
# pip install "paddleocr>=2.0.1"
# PaddleOCR支持的多语言可以通过修改lang参数进行切换，例如'ch', 'en', 'fr', 'german', 'korean', 'japan'
# 以下代码只需运行一次，用于下载并加载模型到内存中

class img2txt():
    def __init__(self):
        # 初始化PaddleOCR对象，设置use_angle_cls为False表示不使用方向分类器，lang设置为"en"表示使用英语模型
        self.ocr = PaddleOCR(use_angle_cls=False, lang="en")

    def rec(self, path):
        # 文字识别函数，接受图片路径作为参数
        """供CV层调用的文字识别函数

        Args:
            path (str): 要识别文字的图片的保存路径
        Returns:
            list: 每行的识别结果
        """
        img_path = path  # 设置图片路径
        result = self.ocr.ocr(img_path, cls=False, det=False)  # 使用PaddleOCR进行文字识别，不进行分类和检测
        rec_res = []  # 初始化识别结果列表
        for idx in range(len(result)):  # 遍历识别结果
            res = result[idx]  # 获取当前行的结果
            for line in res:  # 遍历当前行的每一行
                rec_res.append(line[0])  # 将识别的文本添加到结果列表
        return rec_res  # 返回识别结果

    def locate(self, path):
        # 文字区域定位函数，接受图片路径作为参数
        """供CV层调用的文字区域定位函数

        Args:
            path (str): 要定位文字的图片的保存路径
        Returns:
            list: 文本范围的四个顶点坐标
        """
        img_path = path  # 设置图片路径
        result = self.ocr.ocr(img_path, cls=False)  # 使用PaddleOCR进行文字识别，不进行分类
        loc_res = []  # 初始化定位结果列表
        for idx in range(len(result)):  # 遍历识别结果
            res = result[idx]  # 获取当前行的结果
            for line in res:  # 遍历当前行的每一行
                loc_res.append(line[0])  # 将定位信息添加到结果列表
        return loc_res  # 返回定位结果

# 示例代码
# print(locate('rec/paddleocr/img/test.png'))
