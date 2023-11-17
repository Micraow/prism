from pathlib import Path
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
import sys
qml_file = Path(__file__).parent/"hello.qml"
app = QGuiApplication()
view = QQuickView()

view.setResizeMode(QQuickView.SizeRootObjectToView)
view.setSource(QUrl.fromLocalFile(qml_file.resolve()))
view.show()
sys.exit(app.exec())
del view
