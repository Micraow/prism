#!/bin/bash
python -m venv env
source ./env/bin/activate
pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple
pip install pip -U
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install "paddleocr>=2.0.1"
pip install -r requirements.txt
curl -o model.temp https://alist.pengs.top/d/64816595359b1e5db47f442f901a98ce4efd8481/alist/models/Helsinki-NLP/opus-mt-en-zh/pytorch_model.bin
mv model.temp translate/hf_model/pytorch_model.bin