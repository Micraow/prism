import QtQuick 2.13
import QtQuick.Controls 2.15

Page {
    header: Label {
        id: titlelabel
        text: qsTr("版书记录")
        font.pixelSize: Qt.application.font.pixelSize * 3
        horizontalAlignment: Text.AlignHCenter
        padding: 10
    }
    Label{
        text: qsTr("按下“拍照”键，就能保存版书了")
        horizontalAlignment: Text.AlignHCenter
        anchors.top:titlelabel.bottom
        anchors.topMargin:25
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.horizontalCenter: parent.horizontalCenter
    }
    
}