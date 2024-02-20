import QtQuick 2.13
import QtQuick.Controls 2.15

Page {
    header: Label {
        id: titlelabel
        text: qsTr("错题本")
        font.pixelSize: Qt.application.font.pixelSize * 3
        horizontalAlignment: Text.AlignHCenter
        padding: 10
    }
    Label{
        id: prompt
        text: qsTr("按下“拍照”键，就能保存错题了")
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
            translator.enhancer();
        }
    }

    Label{
        id: result
        text: qsTr("等待事情发生")
        anchors.bottom: parent.bottom
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.horizontalCenter: parent.horizontalCenter
        horizontalAlignment: Text.AlignHCenter
        anchors.bottomMargin: 10
    }

    Connections {
        target: translator
        function onCuoti(results) {
            result.text = results
        }
    }
    
}