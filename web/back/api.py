from flask import Flask, request, jsonify
import sys
import os
from sqlite import get_db, query_db, close_connection  # 从sqlite.py导入必要的函数
from threading import Thread

current_file_dir = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(current_file_dir, "../.."))
sys.path.append(root)
from app import network, backend  # 勿格式化文档！！此行必须在此位置否则导入失败！！

app = Flask(__name__)

# 在app上下文中注册关闭连接的回调
app.teardown_appcontext(close_connection)

now_ID = 0
Backend = backend.Translator(mode=1)  # mode=1 用于web端
res = {}
is_live_translate_running = False  # 新增标志位，用于判断实时翻译是否正在运行

@app.route('/')
def echo_ok():
    return "OK"

@app.route('/network/scan', methods=['GET'])
def scan_wifi():
    return jsonify(network.scan_network())

@app.route('/network/connect', methods=['POST'])
def connect_wifi():
    ssid = request.form['SSID']
    password = request.form['Password']
    result = network.connect_wifi(ssid, password)
    if result is True:
        return jsonify({"Result": "OK"})
    else:
        return jsonify({"Result": "Error"})

@app.route('/network/connected', methods=['GET'])
def getNetworkstatus():
    return jsonify({"Result": network.getNetworkstatus()})

def call_live_translate():
    global now_ID
    global res
    global is_live_translate_running
    res = Backend.liveTranslate()
    db = get_db()
    new_res = {key: value for key, value in res.items() if key != "origin"}
    db.execute("INSERT INTO PRISM (ID, origin, translation) VALUES (?, ?, ?)", [now_ID, res["origin"], str(new_res)])
    db.commit()
    is_live_translate_running = False  # 实时翻译结束后，重置标志位

@app.route('/livetranslate/start', methods=['GET'])
def start_livetranslate():
    global now_ID
    global is_live_translate_running

    if is_live_translate_running:
        return jsonify({"Result": "Fail", "Message": "Live translation is already running", "Ticket": 0})

    try:
        # 从数据库中获取最大的ID并加1
        max_id = query_db("SELECT MAX(ID) FROM PRISM", one=True)
        if max_id and max_id[0] is not None:
            now_ID = max_id[0] + 1
        else:
            now_ID = 1  # 如果数据库为空，从1开始
    except Exception as e:
        print(f"Error fetching max ID: {e}")
        now_ID = 1  # 如果查询失败，从1开始

    is_live_translate_running = True  # 设置标志位，表示实时翻译已启动
    t = Thread(target=call_live_translate)
    t.start()
    return jsonify({"Result": "Success", "Ticket": now_ID})

@app.route('/livetranslate/end', methods=['GET'])
def end_livetranslate():
    global now_ID
    global res
    global is_live_translate_running
    Backend.endLive()
    now_ID = 0
    res = {}
    is_live_translate_running = False  # 重置标志位
    return jsonify({"Result": "Success"})

@app.route('/livetranslate/query', methods=['GET'])
def query_livetranslate():
    global res
    if res:
        return jsonify(res)
    else:
        return jsonify({"Result": "No translation available"})

@app.route('/translate/text', methods=['POST'])
def translate_text():
    content = request.json.get('content')
    provider = request.json.get('provider', 'bing')
    result = Backend.call_backend_simple(content, provider)
    return jsonify({"translation": result})

@app.route('/translate/photo', methods=['GET'])
def translate_photo():
    result = Backend.photoTranslate()
    return jsonify(result)

@app.route('/enhance', methods=['GET'])
def enhance_image():
    result = Backend.enhancer()
    return jsonify({"result": result})

@app.route('/test',methods=['GET'])
def test():
    path = Backend.test_pic()
    return path

@app.route('/history/pai_zhao', methods=['GET'])
def get_pai_zhao_history():
    db = get_db()
    try:
        results = db.execute("SELECT * FROM PRISM WHERE TYPE = 'PIC' ORDER BY ID DESC").fetchall()
        history = []
        for row in results:
            history.append({
                "id": row[0],
                "type": row[1],
                "original_text": row[2],
                "translation": row[3],
                "path": row[4]
            })
        return jsonify(history)
    except Exception as e:
        print(f"Error fetching Pai Zhao history: {e}")
        return jsonify({"Result": "Error", "Message": str(e)})

@app.route('/history/cuo_ti', methods=['GET'])
def get_cuo_ti_history():
    db = get_db()
    try:
        results = db.execute("SELECT * FROM PRISM WHERE TYPE = 'CUOTI' ORDER BY ID DESC").fetchall()
        history = []
        for row in results:
            history.append({
                "id": row[0],
                "type": row[1],
                "path": row[4]
            })
        return jsonify(history)
    except Exception as e:
        print(f"Error fetching Cuo Ti history: {e}")
        return jsonify({"Result": "Error", "Message": str(e)})
    
    
if __name__ == '__main__':
    app.run(debug=True)