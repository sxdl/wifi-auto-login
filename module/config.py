"""
module.py
date: 2023/5/1
description: 
"""
import json
import os
import socket

config = {}


def load_config(config_path="./config.json"):
    global config
    if not os.path.exists(config_path):
        raise Exception('module file not fond.')

    config = read_json(config_path)
    print("load module success.")
    return config


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def user_account():
    return config.get('user').get('user_account')


def user_password():
    return config.get('user').get('user_password')


def ssid():
    return config.get('ssid')


def wlan_ac_ip():
    pass


def url():
    return config.get('request').get('url')


def params():
    auto_ip = config.get('auto_ip')
    p = config.get('request').get('params')
    if auto_ip != "":
        p[auto_ip] = get_local_ip()
    return p


def headers():
    return config.get('request').get('headers')


def get_local_ip():
    return socket.gethostbyname(socket.gethostname())
