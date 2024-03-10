#!/bin/bash
cat <<'END'


  ____       _               
 |  _ \ _ __(_)___ _ __ ___  
 | |_) | '__| / __| '_ ` _ \ 
 |  __/| |  | \__ \ | | | | |
 |_|   |_|  |_|___/_| |_| |_|

 _____________________ 
/ Your personal study \
\ assistant           /
 --------------------- 
   \         ,        ,
    \       /(        )`
     \      \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\
           / /   | `    \
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \
<----|====O)))==) \) /====
<----'    `--' `.__,' \
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \
      `--{__________)        \/

Installing...

有朋自远方来，不亦乐乎。

END

sudo apt update
sudo apt install nodejs npm
npm config set registry http://mirrors.cloud.tencent.com/npm/
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
rm get-pip.py
python -m venv env
source ./env/bin/activate
pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple
pip install pip -U
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install "paddleocr>=2.0.1"
pip install -r requirements.txt
curl -o model.temp https://alist.pengs.top/d/64816595359b1e5db47f442f901a98ce4efd8481/alist/models/Helsinki-NLP/opus-mt-en-zh/pytorch_model.bin
mv model.temp translate/hf_model/pytorch_model.bin

cat <<'END'

 ____________________________ 
< Everything works well 众神归位 >
 ---------------------------- 
                       \                    ^    /^
                        \                  / \  // \
                         \   |\___/|      /   \//  .\
                          \  /O  O  \__  /    //  | \ \           *----*
                            /     /  \/_/    //   |  \  \          \   |
                            @___@`    \/_   //    |   \   \         \/\ \
                           0/0/|       \/_ //     |    \    \         \  \
                       0/0/0/0/|        \///      |     \     \       |  |
                    0/0/0/0/0/_|_ /   (  //       |      \     _\     |  /
                 0/0/0/0/0/0/`/,_ _ _/  ) ; -.    |    _ _\.-~       /   /
                             ,-}        _      *-.|.-~-.           .~    ~
            \     \__/        `/\      /                 ~-. _ .-~      /
             \____(oo)           *.   }            {                   /
             (    (--)          .----~-.\        \-`                 .~
             //__\\  \__ 我是赵陈晨   ///.----..<        \             _ -~
            //    \\               ///-._ _ _ _ _ _ _{^ - - - - ~

END