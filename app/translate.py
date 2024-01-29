from rec.paddleocr import recognize
from CV import cvworker
from PySide6.QtCore import QObject, Signal, Slot
import sys
from translate import bing_dict,bing,deepl,offline,youdao
import network
sys.path.append("./CV")
sys.path.append("./rec")


class translator(QObject):
    def __init__(self):
        super().__init__(self)
        self.worker = cvworker.cv()
        self.img2txt = recognize.img2txt()

    def txt2txt(self,content):
        """调用translate的接口,实现英译中

        Args:
            content (str): 翻译内容
        
        Returns:
            dict: {后端名称:结果}

        """
        result={}
        if network.getNetworkstatus()==True:
            for backend in [bing,deepl,youdao,offline]:
                res=backend.translate(content)
                result[backend.getName()]=res
        
        else:
            backend=offline
            res=backend.translate(content)
            result[backend.getName()]=res
        
        return result

        

    def photoTranslate(self):
        path = self.worker.takePic()
        res=self.img2txt.rec(path)
        string="".join(res)
        return self.txt2txt(string)
