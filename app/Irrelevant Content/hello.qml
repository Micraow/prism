import QtQuick 2.13

Window {
    id: main
    width: 90
    height: 100
    color: "black"
    visible: true
    title: "hello"
    Text {
        text: "hi,world"
        color: "white"
        anchors.top:parent.top
        anchors.topMargin:25
        
        horizontalAlignment: Text.AlignHCenter
        
    }
}
