
# import sys
# from PyQt6.QtWidgets import QWidget, QPushButton, QApplication

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()


#     def initUI(self):

#         qbtn = QPushButton('Quit', self)
#         qbtn.clicked.connect(QApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)

#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle('Quit button')
#         self.show()


# def main():

#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())


# if __name__ == '__main__':
#     main()
import sys
import typing
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """按钮的用例，绑定"""
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(250, 50)

        self.setGeometry(300, 200, 500, 400)
        self.setWindowTitle("EXIT")
        self.show()

    def closeEvent(self, event):
        """对话框（MessageBox的使用"""
        reply = QMessageBox.question(self, "Message", "Exit?", QMessageBox.StandardButton.No|
                            QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if reply == QMessageBox.standardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    exitw = Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
