# -*- coding: UTF-8 -*-
from . import errors


class HandleResult(object):
    """
        HTTP请求统一返回类
    """
    def __init__(self):
        self.success = True
        self.msg = ''
        self.errorCode = 0
        self.result = None

    def opera_fail(self, code: errors.ErrorCode):
        self.success = False
        self.errorCode = code.value
        self.msg = errors.get_error_string(code)
