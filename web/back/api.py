from flask import Flask
from flask import request
import sys
import os
import uuid

current_file_dir = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(current_file_dir, "../.."))
sys.path.append(root)
# print(sys.path)
from app import network, backend  # 勿格式化文档！！此行必须在此位置否则导入失败！！

app = Flask(__name__)

now_UUID = 0
Backend = backend.Translator(mode=1) # mode=1 用于web端

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


@app.route('/network/connected', methods=['GET'])
def getNetworkstatus():
    return {"Result": network.getNetworkstatus()}


@app.route('/livetranslate/start', methods=['GET'])
def start_livetranslate():
    if now_UUID != 0:
        return {"Result": "Fail", "Ticket": 0}

    else:
        now_UUID = uuid.uuid4()
        Backend.liveTranslate()

