import time
import requests
import os


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
    # 调用linux下的networkmanager(nmcli)来做这块
    # 目前的思路是对nmcli的返回结果进行字符串解析
    os.system('nmcli radio wifi on')  # 打开wifi设备
    output = os.popen('nmcli dev wifi list').read()
    output = output.split('\n')
    output = output[1:]
    result = {}
    output.pop()
    for line in output:
        line = line.split()
        if line.pop() == 'WPA1' or 'WPA2':
            need_password = True
        else:
            need_password = False

        if line[0] == '*':
            ssid = line[2]
        else:
            ssid = line[1]
        result[ssid] = {'ssid': ssid, 'need_password': need_password}
    print(result)

    return result


def connect_wifi(ssid: str, password: str):
    '''
    传入SSID和密码尝试连接，即使这个网络没有密码，也收到一个空字符串
    '''
    if password != '':
        os.system('nmcli dev wifi connect '+ssid+' password \"'+password+'\"')

    else:
        os.system('nmcli dev wifi connect '+ssid)

    time.sleep(5)

    return getNetworkstatus()


if __name__ == "__main__":
    scan_network()
