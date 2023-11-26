import QtQuick 2.13
import QtQuick.Controls 2.15

Page {
    header: Label {
        id: titlelabel
        text: qsTr("拍照翻译")
        font.pixelSize: Qt.application.font.pixelSize * 3
        horizontalAlignment: Text.AlignHCenter
        padding: 10
    }
    Label{
        text: qsTr("按下拍照键，即可翻译画面中的文字")
        horizontalAlignment: Text.AlignHCenter
        anchors.top:titlelabel.bottom
        anchors.topMargin:25
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.horizontalCenter: parent.horizontalCenter
    }
    
}