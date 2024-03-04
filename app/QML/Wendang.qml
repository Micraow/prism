import QtQuick 2.13 // 导入Qt Quick模块，用于创建动态界面
import QtQuick.Controls 2.15 // 导入Qt Quick Controls模块，提供用户界面控件

Page { // 定义一个页面作为界面的根元素
    header: Label { // 页面的头部标题
        id: titlelabel // 给标题标签设置一个ID
        text: qsTr("文档录入") // 设置标题文本
        font.pixelSize: Qt.application.font.pixelSize * 3 // 设置字体大小为应用字体大小的三倍
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        padding: 10 // 设置内边距
    }
    Label { // 创建一个标签，用于显示操作提示
        text: qsTr("按下开始键，开始录入，扫描结束后，按“结束”键") // 提示用户如何操作
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        anchors.top: titlelabel.bottom // 将提示标签的顶部锚点到标题标签的底部
        anchors.topMargin: 25 // 设置顶部外边距
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小为应用字体大小的两倍
        anchors.horizontalCenter: parent.horizontalCenter // 水平居中
    }
    Label { // 创建一个标签，用于显示开发状态
        text: qsTr("开发中") // 显示“开发中”文本
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        anchors.top: titlelabel.bottom // 将标签的顶部锚点到标题标签的底部
        anchors.topMargin: 60 // 设置顶部外边距，比操作提示的外边距大
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小为应用字体大小的两倍
        anchors.horizontalCenter: parent.horizontalCenter // 水平居中
    }
}