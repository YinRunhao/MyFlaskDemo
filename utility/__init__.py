# -*- coding: UTF-8 -*-
import json
import datetime


class MyEncoder(json.JSONEncoder):
    """可序列化时间的json编码器
    """
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)
