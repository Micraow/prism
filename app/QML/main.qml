import QtQuick 2.13
import QtQuick.Controls 2.15
import Translator
Window {
    id: root
    visible: true
    width: 900
    height: 600
//     GridLayout {
//         id: main
//         rows: 1
//         anchors.margins: 10
//         anchors.fill: parent
//         clip:true  // 超出边界的进行裁剪，即不显示，默认为false
//         boundsBehavior: Flickable.StopAtBounds  // 滑动不超出父框的大小
//     }
    Translator{
        id: translator
    }

    SwipeView {
        id: swipeView
        anchors.fill: parent
        Welcome{
        }
        //插入子页面
        Huaci {
        }
        Paizhao {
        }
        Cuoti{
        }
    }
    //页码的提示符号
    PageIndicator {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        currentIndex: swipeView.currentIndex
        count: swipeView.count
    }
}
