import sys
from PyQt6.QtWidgets import QApplication, QWidget

def main():
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(200,150)
    w.move(500,500)
    w.setWindowTitle("First 第一次")
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()