import requests

def test_in_mainland_china():
    try:
        # 尝试连接 Google，设置超时时间为 5 秒
        response = requests.get("https://www.google.com", timeout=5)
        # 如果连接成功，返回 False（不在中国大陆）
        return False
    except requests.exceptions.Timeout:
        # 如果超时，返回 True（可能在中国大陆）
        return True
    except requests.exceptions.RequestException as e:
        # 处理其他可能的异常（如网络错误）
        print(f"Error: {e}")
        return True
    
def translate(inputs):
    """not available in mainland China"""
    url = f"http://translate.google.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={inputs}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0][0][0]
    else:
        return "翻译失败"
    
def getName():
    return "google"

# print(translate("I love prism."))