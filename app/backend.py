import sys
import os
current_file_dir = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.append(root+"/CV")
sys.path.append(root+"/rec")
sys.path.append(root+"/translate")

# code above should only be placed here, otherwise import fails

from time import sleep
from threading import Thread
import network
from PySide6.QtCore import QObject, Signal, Slot
import cvworker
import pocr.recognize as recognize
import bing_dict
import bing
import deepl
import offline
import youdao




class Translator(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.worker = cvworker.cv()
        self.img2txt = recognize.img2txt()
        self.photoFlag = False

    pic = Signal(str)
    live = Signal(str)
    cuoti = Signal(str)
    # result = Signal(str, arguments=['provider', 'result'])

    @staticmethod
    def call_backend(content, provider, results):
        try:
            res = provider.translate(content)
            results[provider.getName()] = res
        except:
            results[provider.getName()] = "无结果"

    def txt2txt(self, content: str):
        """调用translate的接口,实现英译中

        Args:
            content (str): 翻译内容

        Returns:
            dict: {后端名称:结果}

        """
        content = content.strip()
        result = {}
        if network.getNetworkstatus() is True:
            if content.isalpha() is not True:
                for backend in [bing, deepl, youdao, offline]:
                    t = Thread(target=self.call_backend,
                               args=(content, backend, result))
                    t.run()
            else:
                backend = bing_dict
                res = backend.explain(content)
                result[backend.getName()] = res
        else:
            backend = offline
            res = backend.translate(content)
            result[backend.getName()] = res

        return result

    @staticmethod
    def result_parser(raw_result):
        result = ""
        for k, v in raw_result:
            result.join([k, ":", v, "\n"])
        return result

    @Slot()
    def photoTranslate(self):
        path = self.worker.takePic()
        res = self.img2txt.rec(path)
        string = "".join(res)
        results = self.result_parser(self.txt2txt(string))
        self.pic.emit(results)

    @Slot()
    def liveTranslate(self):
        back = Thread(target=self._liveTranslate)
        back.run()

    def _liveTranslate(self):
        # self.worker.startCapture(100) # 100ms一张
        images_path = []
        while self.photoFlag:
            path = self.worker.takePic()
            images_path.append(path)
            sleep(0.1)  # 单位是秒
        try:
            path = self.worker.stitch(images_path)
            res = self.img2txt.rec(path)
            string = "".join(res)
            self.live.emit(self.result_parser(self.txt2txt(string)))
        except:
            self.live.emit("无结果")

    @Slot()
    def endLive(self):
        self.photoFlag = False

    @Slot()
    def enhancer(self):
        try:
            self.worker.save(self.worker.enhance(self.worker.takePic()))
            self.cuoti.emit("成功")
        except:
            self.cuoti.emit("失败")
