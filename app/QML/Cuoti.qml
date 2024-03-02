import QtQuick 2.13 // 导入Qt Quick模块，用于创建动态界面
import QtQuick.Controls 2.15 // 导入Qt Quick Controls模块，提供用户界面控件

Page { // 创建一个页面作为界面的根元素
    header: Label { // 页面的标题部分
        id: titlelabel // 给标题标签设置一个ID
        text: qsTr("错题本") // 设置标题文本
        font.pixelSize: Qt.application.font.pixelSize * 3 // 设置字体大小
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        padding: 10 // 设置内边距
    }
    Label { // 创建一个标签，用于显示提示信息
        id: prompt // 设置ID
        text: qsTr("按下“拍照”键，就能保存错题了") // 提示功能
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        anchors.top: titlelabel.bottom // 将提示标签的顶部锚点到标题标签的底部
        anchors.topMargin: 25 // 设置顶部外边距
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小
        anchors.horizontalCenter: parent.horizontalCenter // 水平居中
    }

    RoundButton { // 创建一个圆形按钮，用于拍照功能
        id: startbutton // 设置ID
        text: "拍照" // 设置按钮文本
        anchors.top: prompt.bottom // 将按钮的顶部锚点到提示标签的底部
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小
        anchors.topMargin: 50 // 设置顶部外边距
        anchors.left: parent.left // 将按钮的左侧锚点到父元素的左侧
        anchors.leftMargin: 185 // 设置左侧外边距
        onClicked: { // 当按钮被点击时
            translator.enhancer(); // 调用translator对象的enhancer方法
        }
    }

    Label { // 创建一个标签，用于显示结果
        id: result // 设置ID
        text: qsTr("等待事情发生") // 初始化文本
        anchors.bottom: parent.bottom // 将结果标签的底部锚点到父元素的底部
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小
        anchors.horizontalCenter: parent.horizontalCenter // 水平居中
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        anchors.bottomMargin: 10 // 设置底部外边距
    }

    Connections { // 创建信号连接
        target: translator // 连接的目标对象是translator
        function onCuoti(results) { // 当translator的onCuoti信号被触发时
            result.text = results // 更新结果标签的文本内容
        }
    }
}