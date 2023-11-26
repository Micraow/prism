import QtQuick 2.13
import QtQuick.Controls 2.15

Page {
    id: huaci
    header: Label {
        id: titlelabel
        text: qsTr("划词翻译")
        font.pixelSize: Qt.application.font.pixelSize * 3
        horizontalAlignment: Text.AlignHCenter
        padding: 10
    }
    Label {
        id: prompt
        text: qsTr("按下开始键，开始录入，扫描结束后，按“结束”键")
        horizontalAlignment: Text.AlignHCenter
        anchors.top: titlelabel.bottom
        anchors.topMargin: 25
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.horizontalCenter: parent.horizontalCenter
    }
    RoundButton {
        id: bu1
        text: "开始"
        anchors.top: prompt.bottom
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.topMargin: 50
        anchors.left: parent.left
        anchors.leftMargin: 185
        onClicked: {
            scanning.visible = true;
        }
    }

    RoundButton {
        id: bu2
        text: "结束"
        anchors.top: prompt.bottom
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.topMargin: 50
        anchors.right: parent.right
        anchors.rightMargin: 185
        onClicked: {
            translateresult.visible = true;
            titlelabel.visible = false;
            bu1.visible = false;
            bu2.visible = false;
            prompt.visible = false;
            back.visible = true;
        }
    }

    Text {
        id: scanning
        text: "扫描中，请平行于字行移动，扫描完成按“结束”键"
        visible: false
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 125
        anchors.horizontalCenter: parent.horizontalCenter
        font.pixelSize: Qt.application.font.pixelSize * 2
    }
    Transresult {
        id: translateresult
        visible: false
    }

    Button{
        id: back
        text:"返回"
        visible: false
        anchors.right:parent.right
        anchors.top:parent.top
        anchors.margins: 15
        onClicked:{
            translateresult.visible = false;
            titlelabel.visible = true;
            bu1.visible = true;
            bu2.visible = true;
            prompt.visible = true;
            back.visible = false;
        }
    }
}
