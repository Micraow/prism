import QtQuick 2.13
import QtQuick.Controls 2.15

Page {
    Label {
        id: titlelabel
        text: qsTr("翻译结果")
        anchors.top: parent.top
        font.pixelSize: Qt.application.font.pixelSize * 3
        horizontalAlignment: Text.AlignHCenter
        padding: 10
    }
}
