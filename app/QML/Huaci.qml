import QtQuick 2.13
import QtQuick.Controls 2.15

Page {
    header: Label {
        id: titlelabel
        text: qsTr("划词翻译")
        font.pixelSize: Qt.application.font.pixelSize * 3
        horizontalAlignment: Text.AlignHCenter
        padding: 10
    }
    Label{
        text: qsTr("按下开始键，开始录入，扫描结束后，按“结束”键")
        horizontalAlignment: Text.AlignHCenter
        anchors.top:titlelabel.bottom
        anchors.topMargin:25
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.horizontalCenter: parent.horizontalCenter
    }
    
}
