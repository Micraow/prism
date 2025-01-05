import sys
import os
current_file_dir = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.append(root)
sys.path.append(root+"/CV")
sys.path.append(root+"/rec")
sys.path.append(root+"/translate")

# code above should only be placed here, otherwise import fails

from time import sleep
from threading import Thread
from . import network
import cvworker
import pocr.recognize as recognize
import bing_dict
import bing
import deepl
import offline
import youdao
import google_translate

if network.getNetworkstatus() == False:
    mainland = True
else:
    mainland = google_translate.test_in_mainland_china()

class Translator:
    def __init__(self, mode=0):
        '''
        mode: pyqt为0,web为1
        '''
        self.worker = cvworker.cv()
        self.img2txt = recognize.img2txt()
        self.photoFlag = False
        self.mode = mode
        self.result = {}

    @staticmethod
    def call_backend(content, provider, results):
        try:
            res = provider.translate(content)
            results[provider.getName()] = res
        except:
            results[provider.getName()] = "无结果"

    @staticmethod
    def call_backend_simple(content,provider):
        """**更适合webui的后端调用**

        Args:
            content (str): 内容原文
            provider (str): 翻译供应商["bing", "deepl", "youdao", "offline"]
        """
        match_table={
            "bing":bing,
            "deepl":deepl,
            "youdao":youdao,
            "offline":offline,
            "google":google_translate,
        }

        provider=match_table.get(provider)

        try:
            return provider.translate(content)
        except:
            return "无结果"

    def txt2txt(self, content: str):
        """调用translate的接口,实现英译中

        Args:
            content (str): 翻译内容

        Returns:
            dict: {后端名称:结果}

        """
        content = content.strip()
        result = {}
        result["origin"] = content
        if network.getNetworkstatus() is True:
            if content.isalpha() is not True:
                backends = [bing, deepl, youdao, offline] if mainland else [bing, deepl, youdao, offline, google_translate]
                for backend in backends:
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
            result.join([k, ":", v, "\n"]) # TODO
        return result

    def photoTranslate(self):
        path = self.worker.takePic()
        res = self.img2txt.rec(path)
        string = "".join(res)
        if self.mode == 0:
            results = self.result_parser(self.txt2txt(string))
            return results
        else:
            results = self.txt2txt(string)
            return results

    def liveTranslate(self, var=None):
        self._liveTranslate()
        res = self.result
        return res

    def _liveTranslate(self,var):
        # self.worker.startCapture(100) # 100ms一张
        var = {}
        images_path = []
        while self.photoFlag:
            path = self.worker.takePic()
            images_path.append(path)
            sleep(0.1)  # 单位是秒
        try:
            path = self.worker.stitch(images_path)
            res = self.img2txt.rec(path)
            string = "".join(res)
            if self.mode == 0:
                return self.result_parser(self.txt2txt(string))
            else:
                self.result =  self.txt2txt(string)
                var = self.result
        except:
            if self.mode == 0:
                return "无结果"
            else:
                self.result = {}
                var = {}

    def endLive(self):
        self.photoFlag = False

    def enhancer(self):
        try:
            path = self.worker.save(self.worker.enhance(self.worker.takePic()))
            if self.mode == 0:
                return "成功"
            else:
                return path
        except:
            if self.mode == 0:
                return "失败"
            else:
                return None

    def test_pic(self):
        return self.worker.takePic()