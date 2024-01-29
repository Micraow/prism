from paddleocr import PaddleOCR
# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# need to run only once to download and load model into memory


class img2txt():
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=False, lang="en")

    def rec(self, path):
        """供CV层调用的文字识别函数

        Args:
            path (str): 要识别文字的图片的保存路径，如“rec/paddleocr/img/test.png”
        Returns:
            list: 每行的识别结果
        """
        # img_path = './imgs/test.jpg'
        img_path = path
        result = self.ocr.ocr(img_path, cls=False, det=False)
        rec_res = []
        for idx in range(len(result)):
            res = result[idx]

            for line in res:
                rec_res.append(line[0])
        return rec_res

    def locate(self, path):
        """供CV层调用的文字区域定位函数

        Args:
            path (str): 要定位文字的图片的保存路径，如“rec/paddleocr/img/test.png”
        Returns:
            list: 文本范围的四个顶点坐标
        """
        img_path = path
        result = self.ocr.ocr(img_path, cls=False)
        loc_res = []
        for idx in range(len(result)):
            res = result[idx]

            for line in res:
                loc_res.append(line[0])
        return loc_res

# print(locate('rec/paddleocr/img/test.png'))
