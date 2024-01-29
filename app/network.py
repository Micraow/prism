import requests

def getNetworkstatus():
    '''
    是否联网
    '''
    try:
        requests.get("https://baidu.com")
        return True
    except:
        return False
