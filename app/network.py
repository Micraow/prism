import requests
import pywifi
import json

def getNetworkstatus():
    '''
    是否联网
    '''
    try:
        requests.get("https://baidu.com")
        return True
    except:
        return False
def scanwifi():
    wifi=pywifi.PyWiFi()
    iface=wifi.interface()[0]
    iface.scan()
    results=iface.scan_result()
    ssid=results.ssid.encode("raw_unicode_escape").decode("utf-8")
    a={"ssid":ssid}
    a.dumps()
    return a

    

    

