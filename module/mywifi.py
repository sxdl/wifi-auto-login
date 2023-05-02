"""
mywifi.py
date: 2023/5/1
description: 
"""
import pywifi
from pywifi import const
import time
import requests
import socket
import json
from module import config


def auto_connect():
    # load module
    config.load_config()
    # if connected to Wi-Fi
    while not is_connected():
        connect_network(config.ssid())
    print("网络已连接")
    # if Wi-Fi need login
    if not is_logged_in():
        login(config.user_account(), config.user_password())
    # mywifi.login(config.user_account(), config.user_password())


def is_connected():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    return iface.status() == const.IFACE_CONNECTED


def connect_network(ssid):
    print(f"尝试连接 Wi-Fi: {ssid}")
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_NONE)
    profile.cipher = const.CIPHER_TYPE_NONE

    tep_profile = iface.add_network_profile(profile)
    iface.connect(tep_profile)
    time.sleep(1)


def is_logged_in():
    print("检测网络连接是否正常")
    try:
        requests.get("https://baidu.com", timeout=2)
        print("网络连接正常")
        return True
    except requests.ConnectionError as e:
        print(e)
        print("网络异常，需要登录")
        return False


def login(account, password):
    r = f"https://s2.scut.edu.cn:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&"\
        f"user_account=,0,{account}&user_password={password}&wlan_user_ip={get_local_ip()}&"\
        f"wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=172.25.0.50&wlan_ac_name=AC&"\
        f"jsVersion=3.3.2&v=1818"

    headers = {
        'Host': 's2.scut.edu.cn:801',
        'Referer': 'https://s2.scut.edu.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
    }

    q = requests.get(url=r, headers=headers).text[7:-1]
    re = json.loads(q)
    print(f"result: {re['result']}, msg: {re['msg']}")


def get_local_ip():
    return socket.gethostbyname(socket.gethostname())
