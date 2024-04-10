from flask import Flask
from flask import request
import sys
import os
current_file_dir = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(current_file_dir, "../.."))
sys.path.append(root + "/app")
# print(sys.path)
from app import network # 勿格式化文档！！此行必须在此位置否则导入失败！！

app = Flask(__name__)

now_UUID = 0


@app.route('/')
def echo_ok():
    return "OK"


@app.route('/network/scan', methods=['GET'])
def scan_wifi():
    return network.scan_network()


@app.route('/network/connect', methods=['POST'])
def connect_wifi():
    ssid = request.form['SSID']
    password = request.form['Password']
    result = network.connect_wifi(ssid, password)
    if result is True:
        return {"Result": "OK"}
    else:
        return {"Result": "Error"}
