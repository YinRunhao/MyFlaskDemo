# -*- coding: utf-8 -*-
import configparser
import os

appSetting = configparser.ConfigParser()


def init():
    conf_path = os.path.abspath(__file__)
    conf_path = os.path.dirname(conf_path)
    conf_path = os.path.join(conf_path, 'appSetting.ini')
    appSetting.read(conf_path, encoding='utf-8')
