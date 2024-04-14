from flask import Flask
from flask import request
import sys
import os
import sqlite # 不是python内置的sqlite3
from threading import Thread

current_file_dir = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(current_file_dir, "../.."))
sys.path.append(root)
# print(sys.path)
from app import network, backend  # 勿格式化文档！！此行必须在此位置否则导入失败！！

app = Flask(__name__)

now_ID = 0
Backend = backend.Translator(mode=1) # mode=1 用于web端
res = {}

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

def call_live_translate():
    global now_ID
    global res
    res = Backend.liveTranslate()
    db = sqlite.get_db()
    new_res = {key: value for key, value in res.items() if key != "origin"}
    db.execute("INSERT INTO PRISM (?)",[now_ID,res["origin"],new_res])


@app.route('/livetranslate/start', methods=['GET'])
def start_livetranslate():
    global now_ID
    if now_ID != 0:
        return {"Result": "Fail", "Ticket": 0}

    else:
        try:
            now_ID = sqlite.query_db("SELECT ID FROM PRISM ORDERED BY ID DESC",one=True) + 1
        except:
            now_ID = 1 # 第一次用，没有已有记录
        t = Thread(target=call_live_translate)
        t.start()
        return {"Result": "Success", "Ticket": now_ID}


# 注意：end端点需要将now_ID设为0,query端点需要将全局变量res设为空