# -*- coding: utf-8 -*-
import os
import logging
import logging.config
import logging.handlers as handlers
from ..config import appSetting

logger = logging.getLogger()


def init():
    # 日志等级
    logLv = appSetting.get('Log', 'Level')
    level = logging.getLevelName(logLv.upper())
    logger.setLevel(level)

    # 日志格式
    log_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    formatter = logging.Formatter(log_fmt)

    # 日志保留天数
    keepDays = appSetting.getint('Log', 'KeepDays')
    logPath = appSetting.get('Log', 'LogPath')

    # 保证日志文件夹存在
    dirPath = os.path.dirname(logPath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    # 日志处理器
    handler = handlers.TimedRotatingFileHandler(filename=logPath, when='D', backupCount=keepDays, encoding='utf-8')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
