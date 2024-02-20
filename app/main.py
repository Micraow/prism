from pathlib import Path
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
import sys
import backend
qml_file = Path(__file__).parent/"QML/main.qml"
app = QGuiApplication(sys.argv)
view = QQmlApplicationEngine()
# translator=backend.translator()
qmlRegisterType(backend.Translator,'Translator',1,0,'Translator')

view.load(QUrl.fromLocalFile(qml_file.resolve()))
sys.exit(app.exec())
del view
