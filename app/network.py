import requests
import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]


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
    iface.scan()
    time.sleep(5) # Note. Because the scan time for each Wi-Fi interface is variant. It is safer to call scan_results() 2 ~ 8 seconds later after calling scan().
    results=iface.scan_results()
    ssid = []
    for i in results:
        name=i.ssid.encode("raw_unicode_escape").decode("utf-8")
        # pywifi无法获取是否需要密码，那也是个过时的库了
        # 我现在的想法是不用pywifi而用python去运行一些shell命令
        # 调用linux下的networkmanager来做这块
        ssid.append(name)

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
