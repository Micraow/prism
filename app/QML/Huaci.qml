import QtQuick 2.13 // 导入Qt Quick模块，用于创建动态界面
import QtQuick.Controls 2.15 // 导入Qt Quick Controls模块，提供用户界面控件

Page { // 定义一个页面作为界面的根元素
    id: huaci // 给页面设置一个ID
    header: Label { // 页面的标题部分
        id: titlelabel // 设置标题标签的ID
        text: qsTr("划词翻译") // 设置标题文本
        font.pixelSize: Qt.application.font.pixelSize * 3 // 设置字体大小
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        padding: 10 // 设置内边距
    }
    Label { // 创建一个标签，用于显示操作提示
        id: prompt // 设置提示标签的ID
        text: qsTr("按下开始键，开始录入，扫描结束后，按“结束”键") // 提示用户如何操作
        horizontalAlignment: Text.AlignHCenter // 文本水平居中
        anchors.top: titlelabel.bottom // 将提示标签的顶部锚点到标题标签的底部
        anchors.topMargin: 25 // 设置顶部外边距
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小
        anchors.horizontalCenter: parent.horizontalCenter // 水平居中
    }
    RoundButton { // 创建一个圆形按钮，用于开始扫描
        id: bu1 // 设置开始按钮的ID
        text: "开始" // 设置按钮文本
        anchors.top: prompt.bottom // 将按钮的顶部锚点到提示标签的底部
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小
        anchors.topMargin: 50 // 设置顶部外边距
        anchors.left: parent.left // 将按钮的左侧锚点到父元素的左侧
        anchors.leftMargin: 185 // 设置左侧外边距
        onClicked: { // 当按钮被点击时
            scanning.visible = true; // 显示扫描提示文本
            translator.liveTranslate(); // 调用翻译器的实时翻译功能
        }
    }

    RoundButton { // 创建一个圆形按钮，用于结束扫描
        id: bu2 // 设置结束按钮的ID
        text: "结束" // 设置按钮文本
        anchors.top: prompt.bottom // 将按钮的顶部锚点到提示标签的底部
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小
        anchors.topMargin: 50 // 设置顶部外边距
        anchors.right: parent.right // 将按钮的右侧锚点到父元素的右侧
        anchors.rightMargin: 185 // 设置右侧外边距
        onClicked: { // 当按钮被点击时
            translateresult.visible = true; // 显示翻译结果
            titlelabel.visible = false; // 隐藏标题
            bu1.visible = false; // 隐藏开始按钮
            bu2.visible = false; // 隐藏结束按钮
            prompt.visible = false; // 隐藏提示
            back.visible = true; // 显示返回按钮
            translator.endLive(); // 结束实时翻译
        }
    }

    Text { // 创建一个文本元素，用于显示扫描状态
        id: scanning // 设置扫描状态文本的ID
        text: "扫描中，请平行于字行移动，扫描完成按“结束”键" // 设置文本内容
        visible: false // 默认不可见
        anchors.bottom: parent.bottom // 将文本的底部锚点到父元素的底部
        anchors.bottomMargin: 125 // 设置底部外边距
        anchors.horizontalCenter: parent.horizontalCenter // 水平居中
        font.pixelSize: Qt.application.font.pixelSize * 2 // 设置字体大小
    }
    Transresult { // 创建一个翻译结果组件
        id: translateresult // 设置翻译结果组件的ID
        visible: false // 默认不可见
    }

    Button { // 创建一个按钮，用于返回上一级
        id: back // 设置返回按钮的ID
        text: "返回" // 设置按钮文本
        visible: false // 默认不可见
        anchors.right: parent.right // 将按钮的右侧锚点到父元素的右侧
        anchors.top: parent.top // 将按钮的顶部锚点到父元素的顶部
        anchors.margins: 15 // 设置外边距
        onClicked: { // 当按钮被点击时
            translateresult.visible = false; // 隐藏翻译结果
            titlelabel.visible = true; // 显示标题
            bu1.visible = true; // 显示开始按钮
            bu2.visible = true; // 显示结束按钮
            prompt.visible = true; // 显示提示
            back.visible = false; // 隐藏返回按钮
        }
    }

    Connections { // 创建信号连接
        target: translator // 连接的目标对象是translator
        function onLive(results) { // 当translator的onLive信号被触发时
            translateresult.resultlabel.text = results; // 更新翻译结果组件的文本内容
        }
    }
}