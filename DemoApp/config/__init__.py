# -*- coding: utf-8 -*-
import configparser
import os

# 提供给外部调用的实例
appSetting = configparser.ConfigParser()


def init():
    # 拼接配置文件地址
    conf_path = os.path.abspath(__file__)
    conf_path = os.path.dirname(conf_path)
    conf_path = os.path.join(conf_path, 'appSetting.ini')
    # 读取配置文件
    appSetting.read(conf_path, encoding='utf-8')
