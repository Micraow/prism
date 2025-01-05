#!/bin/bash
cat <<'END'
  ____       _               
 |  _ \ _ __(_)___ _ __ ___  
 | |_) | '__| / __| '_ ` _ \ 
 |  __/| |  | \__ \ | | | | |
 |_|   |_|  |_|___/_| |_| |_|

web branch

Installing...

有朋自远方来，不亦乐乎。

END


sudo apt update
sudo apt install nodejs npm network-manager
sudo systemctl start NetworkManager.service
sudo apt install -y nodejs npm network-manager
sudo systemctl start NetworkManager.service 
sudo systemctl enable NetworkManager.service
npm config set registry http://mirrors.cloud.tencent.com/npm/
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple

# Install conda if not already installed
if ! command -v conda &> /dev/null; then
    echo "Conda not found. Installing Miniconda..."
    curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
    rm Miniconda3-latest-Linux-x86_64.sh
    export PATH="$HOME/miniconda/bin:$PATH"
    conda init bash
    source ~/.bashrc
fi

# Set up conda channels
conda config --add channels https://mirrors.nju.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.nju.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.nju.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.nju.edu.cn/anaconda/cloud/Paddle
conda config --set show_channel_urls yes
conda create --name prism_env --file ./requirements.txt
conda activate prism_env
pip install paddleocr

curl -o model.temp https://hf-mirror.com/Helsinki-NLP/opus-mt-en-zh/resolve/main/pytorch_model.bin?download=true
mv model.temp translate/hf_model/pytorch_model.bin

cd web/front/prism-web && npm install && cd -

cat <<'END'

< Everything works well 众神归位 >

本分支由Pengbo (micraow)维护
END