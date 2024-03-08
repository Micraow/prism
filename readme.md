<h1 align="center">Prism  👋</h1>
<div align="center">
<p><a href="https://github.com/micraow/prism">Github Repo</a> · <a href="https://gitee.com/micraow/prism">Gitee Repo</a> · <a href="https://pengs.top/">Peng's Blog</a></p>
<p><em>你的私人学习助手</em></p>
</div>

![GitHub language count](https://img.shields.io/github/languages/count/micraow/prism?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/micraow/prism?style=for-the-badge&logo=python)
![GitHub License](https://img.shields.io/github/license/micraow/prism?style=for-the-badge&logo=gnu&logoColor=gnu)
![GitHub repo size](https://img.shields.io/github/repo-size/micraow/prism?style=for-the-badge&logo=gnubash&logoColor=%23000000&labelColor=%234EAA25&color=%23008DE4)
![GitHub forks](https://img.shields.io/github/forks/micraow/prism?style=for-the-badge&logo=github)
![GitHub Repo stars](https://img.shields.io/github/stars/micraow/prism?style=for-the-badge&logo=github)
[![DeepSource](https://app.deepsource.com/gh/Micraow/prism.svg/?label=active+issues&show_trend=true&token=HyakmGyrHNo6ZnZyzynFzddU)](https://app.deepsource.com/gh/Micraow/prism/)

![linux](https://img.shields.io/badge/linux-%23FCC624?style=for-the-badge&logo=linux&logoColor=%23000000)
![Qt](https://img.shields.io/badge/Qt-%2341CD52?style=for-the-badge&logo=qt&logoColor=%23000000)
![OpenCV](https://img.shields.io/badge/OpenCV-%235C3EE8?style=for-the-badge&logo=opencv&logoColor=%23FFFFFF)
![PaddleOCR](https://img.shields.io/badge/PaddleOCR-%230062B0?style=for-the-badge&logo=paddlepaddle&logoColor=%23FFFFFF)
![VScode](https://img.shields.io/badge/VScode-%23007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=%23FFFFFF)

![JLHS](https://img.shields.io/badge/Developed_in-JLHS-blue?style=for-the-badge&logo=educative)
![love](https://img.shields.io/badge/Made_with-love-red?style=for-the-badge&logo=heart)


Prism 是 南京市金陵中学学生研究性学习 项目，本项目的目标是构建基于计算机视觉与深度学习技术的linux平台开源学习辅助软件。

我们的项目涉及计算机视觉，深度学习，应用开发，linux，电子电路等多个方面的知识，预期在1年内完成。

项目的作者包括 **彭勃(micraow),赵陈晨，沈锦良（锦芸Offical），盛宇博（星辰宇宙）**

分工：

    彭勃：总制作者，主要程序的编写与技术指导

    赵陈晨：前端web化重构

    沈锦良：代码注释与报告撰写等

    盛宇博：代码修复与细节改进

本项目基于GPL-2.0协议开源，商业使用请先联系我们！

[开发文档](https://gitee.com/micraow/prism/tree/master/docs)

## 目标功能
使用摄像模块在待识别文字上划过，通过API调用第三方翻译服务，将对应中文显示在屏幕上。要求能在一定程度上克服因纸张或字体风格（斜体、花体等）而造成的识别困难。


**系统层** ：下载所提供linux下的一键安装脚本


**预处理** ：1.以合适的速率从摄像头获取画面，合成为一张图像

2.对图像进行增强锐化（加对比度，二值化，黑白处理，淡化背景等）

3.校正因拍摄造成的变形（几何投射变换）

4.根据单词，对图像进行分割，运用模型识别


**模型** ：接收预处理后的图像，识别成文字


**翻译** ：1.与多个翻译后端对接，获取多家翻译。对于句子返回译文，对于单词返回词典释义

2.提供本地离线翻译模型


**应用层** ：1.提示用户时间，日期，电量，引导用户连接WiFi

2.功能菜单


a.扫描翻译（扫描上传图片上的文字并翻译）

b.拍摄翻译（用摄像头拍照并翻译）

c.文档录入（从纸上扫过或拍摄文档，将其识别后保存）

d.板书保存（不要求识别，只要矫正变形，改变一下背景颜色即可）

e.错题保存


3.在用户扫描单词或拍摄照片时，引导其操作

4.协调调用各层所提供的接口，并以多线程异步的方式进行，提高效率（比如一边扫描一边预处理和识别）



## 技术方案
**系统层**：提供linux下的一键安装脚本

**应用层**：使用PySide6开发,使用Qt Quick技术，利用QML设计界面

**采集与预处理** ：从相机模块获取画面（视频或连拍的照片）。首先将单词与单词分隔，再将每个字母分出来，并进行画面校正，提高对比度，去除噪声。

        所需知识：PIL，Opencv，Python（必须）

        出现的问题：如何从连续的照片或视频中确定镜头的相对位置，避免重复或漏扫？

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

        所需知识：Qt Quick，QML，PySide6，Python，Linux界面设计，Linux显示，Linux网络连接，json，多线程

        可能出现的问题：中文显示有误（同时需要更适合小屏幕，弱性能设备的框架）

**其它基础知识**

    1.Markdown（用于写文档）2.git（版本控制）

## 使用方法

### linux
linux用户初次使用请运行：

```bash
git clone https://gitee.com/micraow/prism.git
cd prism
chmod +x install.sh
sudo bash install.sh
python app/main.py
```
此后：

```bash
cd prism
source ./env/bin/activate
python app/main.py
```

### Windows用户：

首先，开机，然后联网

1. 下载git
2. 打开git shell
3. 输入： git clone https://gitee.com/micraow/prism.git
4. 回车（嘲讽某些不回车的）
5. 打开浏览器，输入https://www.python.org/downloads/windows/
6. 找到最新的安装包下载（不知道选哪种架构就选64-bit）
7. 安装刚刚下载的包，注意添加PATH变量
8. 下载https://bootstrap.pypa.io/get-pip.py到一个文件夹
9. 在那个文件夹打开git shell（按住shift然后右键就能看到了）
10. 输入python get-pip.py并回车
11. 在prism文件夹下打开git shell
12. python -m venv env
13. source ./env/bin/activate
14. 不想写了，自己打开install.sh看看，运行从`pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple`到`pip install -r requirements.txt`间的命令
15. 打开浏览器，输入https://alist.pengs.top/d/64816595359b1e5db47f442f901a98ce4efd8481/alist/models/Helsinki-NLP/opus-mt-en-zh/pytorch_model.bin 把它下载下来
16. 确保文件名为pytorch_model.bin
17. 把该文件移动到translate/hf_model/下
18. 在项目根目录的git shell里运行python app/main.py

以后运行：

<你如果能做到这一步，则你已经有了一定的shell使用经验，参照上方linux的命令即可>

### 更新程序：

```bash
git pull
```

再也不想给windows用户写文档了...

## 不足之处

目前，后端还不稳定，有时不能正确处理复杂环境下的图像，且合并、识别用时长。

翻译时，虽然是多线程同时翻译，但是必须要等到最后一个线程结束才返回结果，不是很好。

## 联系方式

你可以联系我（彭勃）

我的邮箱是： peng@pengs.top

我的网站是 pengs.top,上面有更多的联系方法。

也欢迎向本项目捐赠！

## 参阅文献

[1]项璟,张汝峰,褚俊英等.结合横向投影和仿射变换的文本图像倾斜矫正[J].造纸装备及材料,2020,49(02):251.

[2]王咸锋,黄妙燕.基于OpenCV实现文档物体的纠偏方法[J].电脑知识与技术,2016,12(24):87-89.DOI:10.14004/j.cnki.ckt.2016.3312.

[3]孙丹阳,邵坤艳,孙春志等.基于图像处理的文档图像矫正系统研究与设计[J].电脑与信息技术,2023,31(03):20-23.DOI:10.19414/j.cnki.1005-1228.2023.03.008.

[4]Wang Q, Li B, Xiao T, et al. Learning deep transformer models for machine translation[J]. arXiv preprint arXiv:1906.01787, 2019.

[5]Ghimire D. Comparative study on Python web frameworks: Flask and Django[J]. 2020.