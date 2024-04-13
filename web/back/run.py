# 该脚本启动flask服务器，仅适用于linux,经过测试
import os
current_file_dir = os.path.dirname(__file__)
os.system('cd '+current_file_dir+'&&export FLASK_APP=api.py&&flask run')
