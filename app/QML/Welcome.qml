import QtQuick 2.13
import QtQuick.Controls 2.15
Page {
    //显示
    Label {
        id: textDateTime
        text: currentDateTime()
        font.pixelSize: Qt.application.font.pixelSize * 6
        anchors.centerIn: parent
    }
    Label{
        id: welcomer
        text: qsTr("Prism 您的专属学习助手")
        font.pixelSize: Qt.application.font.pixelSize * 2
        anchors.horizontalCenter: textDateTime.horizontalCenter
        padding: 15
    }


    //当前日期时间
    function currentDateTime() {
        return Qt.formatDateTime(new Date(), "yyyy-MM-dd hh:mm:ss ddd");
    }

    //定时器
    Timer {
        id: timer
        interval: 1000 //间隔(单位毫秒):1000毫秒=1秒
        repeat: true //重复
        onTriggered: {
            textDateTime.text = currentDateTime();
        }
    }

    Component.onCompleted: {
        timer.start();
    }
}

/*
Text元素用来显示日期时间,
currentDateTime函数用来获取当前日期时间,
Timer元素用来定时刷新,实现动态呈现.
*/
