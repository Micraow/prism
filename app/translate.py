from rec.paddleocr import recognize
from CV import cvworker
from PySide6.QtCore import QObject, Signal, Slot
import sys
from translate import bing_dict, bing, deepl, offline, youdao
import network
from time import sleep
sys.path.append("./CV")
sys.path.append("./rec")


class translator(QObject):
    def __init__(self):
        super().__init__(self)
        self.worker = cvworker.cv()
        self.img2txt = recognize.img2txt()
        self.photoFlag = False

    def txt2txt(self, content: str):
        """调用translate的接口,实现英译中

        Args:
            content (str): 翻译内容

        Returns:
            dict: {后端名称:结果}

        """
        content = content.strip()
        result = {}
        if network.getNetworkstatus() == True:
            if content.isalpha() != True:
                for backend in [bing, deepl, youdao, offline]:
                    res = backend.translate(content)
                    result[backend.getName()] = res
            else:
                backend = bing_dict
                res = backend.explain(content)
                result[backend.getName()] = res
        else:
            backend = offline
            res = backend.translate(content)
            result[backend.getName()] = res

        return result

    def photoTranslate(self):
        path = self.worker.takePic()
        res = self.img2txt.rec(path)
        string = "".join(res)
        return self.txt2txt(string)

    def liveTranslate(self):
        # self.worker.startCapture(100) # 100ms一张
        images_path = []
        while self.photoFlag:
            path = self.worker.takePic()
            images_path.append(path)
            sleep(0.1)  # 单位是秒
        path = self.worker.stitch(images_path)
        res = self.img2txt.rec(path)
        string = "".join(res)
        return self.txt2txt(string)
