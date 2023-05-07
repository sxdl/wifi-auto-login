"""
mywifi.py
date: 2023/5/1
description: 
"""
import pywifi
from pywifi import const
import time
import requests
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
        login()


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
    except requests.ConnectionError:
        # print(e)
        print("网络异常，需要登录")
        return False


def login():
    url = config.url()
    params = config.params()
    headers = config.headers()

    q = requests.get(url=url, params=params, headers=headers).text[7:-1]
    re = json.loads(q)
    print(f"result: {re['result']}, msg: {re['msg']}")
