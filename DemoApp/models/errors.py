import enum


class ErrorCode(enum.Enum):
    OK = 0
    # 登录失败
    LoginFail = 101
    # 资源未找到
    ResourceNotFound = 102
    # 遇到异常
    ServerError = 201
    # 参数错误
    ParameterErr = 301


def get_error_string(code: ErrorCode) -> str:
    ret = ''
    if code == ErrorCode.LoginFail:
        ret = 'User name or password incorrect'
    elif code == ErrorCode.ParameterErr:
        ret = 'Parameter parse error'
    elif code == ErrorCode.ResourceNotFound:
        ret = 'Resource not found'
    elif code == ErrorCode.ServerError:
        ret = 'Server meet some exception'

    return ret
