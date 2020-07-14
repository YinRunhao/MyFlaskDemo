# -*- coding: utf-8 -*-
from ..result import HandleResult
from ..errors import ErrorCode
from ..services import user_service
from ..services import article_service
from ...log import logger


def check_user(usrNm: str, psd: str) -> HandleResult:
    """
        检查用户信息是否合法
    """
    result = HandleResult()
    try:
        if usrNm is None or psd is None:
            result.opera_fail(ErrorCode.ParameterErr)
        else:
            dto = user_service.get_user_info(usrNm, psd)
            if dto is not None:
                result.result = dto
            else:
                result.opera_fail(ErrorCode.LoginFail)
    except Exception:
        # 记录错误日志(会自动记录调用堆栈)
        logger.exception('catch some exception')
        result.opera_fail(ErrorCode.ServerError)

    return result


def get_user_articles(usrNm: str) -> HandleResult:
    """
        获取用户所有文章
    """
    result = HandleResult()

    try:
        usrId = user_service.get_user_id(usrNm)
        if usrId > 0:
            lst = article_service.get_user_articles(usrId)
            result.result = lst
        else:
            result.opera_fail(ErrorCode.ResourceNotFound)
    except Exception:
        # 记录错误日志(会自动记录调用堆栈)
        logger.exception('catch some exception')
        result.opera_fail(ErrorCode.ServerError)
    return result
