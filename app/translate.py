from PySide6.QtCore import QObject, Signal, Slot
import sys
sys.path.append("./CV")
sys.path.append("./rec")
from CV import cvworker
from rec.paddleocr import recognize

class translator(QObject):
    def __init__(self):
        super().__init__(self)
        worker=cvworker.cv()
    
    


