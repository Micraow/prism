import sys
import os
current_file_dir = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.append(root+"/CV")
sys.path.append(root+"/rec")
sys.path.append(root+"/translate")
import youdao
import offline
import deepl
import bing
import bing_dict
import pocr.recognize as recognize
import cvworker
from PySide6.QtCore import QObject, Signal, Slot
import network
from threading import Thread
from time import sleep



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
                    try:
                        res = backend.translate(content)
                        result[backend.getName()] = res
                    except:
                        result[backend.getName()] = "无结果"
            else:
                backend = bing_dict
                res = backend.explain(content)
                result[backend.getName()] = res
        else:
            backend = offline
            res = backend.translate(content)
            result[backend.getName()] = res

        return result

    @Slot()
    def photoTranslate(self):
        path = self.worker.takePic()
        res = self.img2txt.rec(path)
        string = "".join(res)
        results = str(self.txt2txt(string))
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
            self.live.emit(str(self.txt2txt(string)))
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