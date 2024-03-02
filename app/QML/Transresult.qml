import QtQuick 2.13 // 导入Qt Quick模块，用于创建动态界面
import QtQuick.Controls 2.15 // 导入Qt Quick Controls模块，提供用户界面控件

Page { // 定义一个页面作为界面的根元素
    Label { // 创建一个标签，用作页面的标题
        id: titlelabel // 给标题标签设置一个ID
        text: qsTr("翻译结果") // 设置标题文本
        anchors.top: parent.top // 将标题标签的顶部锚点到父元素（页面）的顶部
        font.pixelSize: Qt.application.font.pixelSize * 3 // 设置字体大小为应用字体大小的三倍
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        padding: 10 // 设置内边距
    }
    Label { // 创建一个标签，用于显示翻译结果或当前状态
        id: resultlabel // 给结果标签设置一个ID
        text: qsTr("请耐心等待") // 显示提示文本，告知用户等待翻译结果
        anchors.top: titlelabel.bottom // 将结果标签的顶部锚点到标题标签的底部
        font.pixelSize: Qt.application.font.pixelSize * 3 // 设置字体大小为应用字体大小的三倍
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        padding: 10 // 设置内边距
    }
}
