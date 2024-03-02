import QtQuick 2.13
import QtQuick.Controls 2.15

// 定义页面，作为应用程序的主界面
Page {
    // 页面的标题栏，显示为一个Label
    header: Label {
        id: titlelabel 
        text: qsTr("拍照翻译")
        font.pixelSize: Qt.application.font.pixelSize * 3 // 设置标题字体大小
        horizontalAlignment: Text.AlignHCenter // 标题文本居中显示
        padding: 10 // 设置标题的内边距
    }
    // 提示信息标签，告诉用户如何使用应用
    Label{
        id: prompt // 提示标签的ID
        text: qsTr("按下拍照键，即可翻译画面中的文字") // 提示用户如何操作
        horizontalAlignment: Text.AlignHCenter // 提示文本居中显示
        anchors.top: titlelabel.bottom // 提示标签位于标题标签下方
        anchors.topMargin: 25 // 提示标签与标题标签之间的间距
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置提示字体大小
        anchors.horizontalCenter: parent.horizontalCenter // 提示标签水平居中
    }
    // 拍照按钮，用户点击后触发拍照翻译功能
    RoundButton {
        id: startbutton 
        text: "拍照" // 显示的文本
        anchors.top: prompt.bottom // 按钮位于提示标签下方
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置按钮字体大小
        anchors.topMargin: 50 // 按钮与提示标签之间的间距
        anchors.left: parent.left // 按钮左侧与父元素左侧对齐
        anchors.leftMargin: 185 // 按钮左侧的外边距
        onClicked: { // 点击时执行函数
            translator.photoTranslate(); // 调用翻译器的拍照翻译方法
        }
    }

    // 显示翻译结果的标签
    Label {
        id: result // 
        anchors.top: startbutton.bottom // 结果标签位于拍照按钮下方
        anchors.topMargin: 50 // 结果标签与拍照按钮之间的间距
        anchors.horizontalCenter: parent.horizontalCenter // 结果标签水平居中
        text: "请先拍照" // 初始化显示的文本
    }

    // 连接翻译器对象，监听翻译结果信号
    Connections {
        target: translator // 设置连接的目标对象为翻译器
        function onPic(results) { // 当翻译器的onPic信号被触发时执行的函数
            result.text = results // 更新结果标签的文本为翻译结果
        }
    }
}