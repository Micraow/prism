## Prism

Prism 是 南京市金陵中学学生研究性学习项目，本项目的目标是构建基于深度学习和linux平台实现的文字扫描翻译硬件，类似于翻译笔。

我们的项目涉及计算机视觉，深度学习，应用开发，linux，电子电路等多个方面的知识，预期在1年内完成。

项目的作者包括 **彭勃(micraow),赵陈晨，盛宇博，孙延，沈锦良**

本项目基于GPL-2.0协议开源，商业使用请先联系我们！

[开发文档](https://gitee.com/micraow/prism/tree/master/docs)

## 技术方案
功能：使用摄像模块在待识别文字上划过，通过API调用第三方翻译服务，将对应中文显示在屏幕上。要求能在一定程度上克服因纸张或字体风格（斜体、花体等）而造成的识别困难。

[]分层：
**硬件**：考虑树莓派Zero2W，要能上网，有相机模块，显示模块，可能需要LED用以照明纸张。

        所需知识：Linux，电子电路，光学相关知识

**采集与预处理** ：从相机模块获取画面（视频或连拍的照片）。首先将单词与单词分隔，再将每个字母分出来，并进行画面校正，提高对比度，去除噪声。

        所需知识：PIL，Opencv，Python（必须）

        可能出现的问题：如何从连续的照片或视频中确定镜头的相对位置，避免重复或漏扫？

                e.g.  a.I have a cat.

                     b.I have a cat.     

                       I have have a cat.

         解决方案：参照全景照片用Opencv实现

**模型** ：从输入的图片预测该字母（或数字，或标点）

        所需知识：pytorch，卷积神经网络，深度学习，Python

        可能出现的问题：如何适应多种字体？

         解决方案：印刷和手写字体分别处理？准备多种模型？

**翻译层** ：与第三方在线翻译服务交互，返回翻译结果。

        所需知识：requests，json，http，python

**显示（大前端）** ：一个开销小，流畅，美观的与用户交互的UI

        所需知识：GTK/Qt，Python/C++，Linux界面设计，Linux显示，Linux网络连接，json

        可能出现的问题：中文显示有误（同时需要更适合小屏幕，弱性能设备的框架）

[]**其它**

所有人都应会的知识：

    Markdown（用于写文档）2.git（版本控制）

阶段：

    Stage1：本学期期末前完成所有基本功能，能较好实现印刷字体识别，同时有基本界面。

    Stage2：完善手写识别与抗干扰能力，美化界面，如有可能3D打印一个外壳。






**硬件** ：1.组装好，装好系统，载入程序，开机自动启动GUI

2.含摄像头和电池。摄像头的位置应设置成纸面和远处都可以对焦清楚（也许需要一些额外的光学元件）


**预处理** ：1.以合适的速率从摄像头获取画面，合成为一张图像

2.对图像进行增强锐化（加对比度，二值化，黑白处理，淡化背景）

3.校正因拍摄造成的变形（几何投射变换）

4.根据单词，对图像进行分割，运用模型识别


**模型** ：接收预处理后的图像，识别成文字


**翻译** ：1.与多个翻译后端对接，获取多家翻译。对于句子返回译文，对于单词返回词典释义

2.提供本地离线翻译模型


**应用层** ：1.提示用户时间，日期，电量，引导用户连接WiFi

2.功能菜单
[]

a.扫描翻译

b.拍摄翻译

c.文档录入（从纸上扫过或拍摄文档，将其识别后保存）

d.板书保存（不要求识别，只要矫正变形，改变一下背景颜色即可）

e.错题保存


3.在用户扫描单词或拍摄照片时，引导其操作

4.协调调用各层所提供的接口，并以多线程异步的方式进行，提高效率（比如一边扫描一边预处理和识别）