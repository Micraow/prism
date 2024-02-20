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
        id: prompt
        horizontalAlignment: Text.AlignHCenter
        anchors.top:titlelabel.bottom
        anchors.topMargin:25
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.horizontalCenter: parent.horizontalCenter
    }
    RoundButton {
        id: startbutton
        text: "拍照"
        anchors.top: prompt.bottom
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.topMargin: 50
        anchors.left: parent.left
        anchors.leftMargin: 185
        onClicked: {
            translator.photoTranslate();
        }
    }

    Label {
        id: result
        anchors.top: startbutton.bottom
        anchors.topMargin: 50
        anchors.horizontalCenter: parent.horizontalCenter
        text: "请先拍照"
    }

    Connections {
        target: translator
        function onPic(results) {
            result.text = results
        }
    }
}