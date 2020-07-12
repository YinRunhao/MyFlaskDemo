# -*- coding: utf-8 -*-
from ..result import HandleResult
from ..errors import ErrorCode
from ..services import user_service


def check_user(usrNm: str, psd: str) -> HandleResult:
    """
        检查用户信息是否合法
    """
    result = HandleResult()
    if usrNm is None or psd is None:
        result.opera_fail(ErrorCode.ParameterErr)
    else:
        dto = user_service.get_user_info(usrNm, psd)
        if dto is not None:
            result.result = dto
        else:
            result.opera_fail(ErrorCode.LoginFail)
    return result
