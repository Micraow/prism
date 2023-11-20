from pathlib import Path
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
import sys
qml_file = Path(__file__).parent/"hello.qml"
app = QGuiApplication()
view = QQmlApplicationEngine()


view.load(QUrl.fromLocalFile(qml_file.resolve()))
sys.exit(app.exec())
del view
