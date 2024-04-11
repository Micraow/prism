import requests
import pywifi
import time


def getNetworkstatus():
    '''
    是否联网
    '''
    try:
        requests.get("https://baidu.com")
        return True
    except:
        return False


def scan_network():
    '''
    扫描附近局域网，返回SSID和是否需要密码
    '''
    # pywifi无法获取是否需要密码，那也是个过时的库了
    # 调用linux下的networkmanager来做这块
    return {}  # TODO


def connect_wifi(ssid: str, password: str):
    '''
    传入SSID和密码尝试连接，即使这个网络没有密码，也收到一个空字符串
    '''
    # TODO 你调用PyWiFi来连接
    state = True
    return state


if __name__ == "__main__":
    scan_network()
