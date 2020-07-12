import enum


class ErrorCode(enum.Enum):
    OK = 0
    # 登录失败
    LoginFail = 101
    # 参数错误
    ParameterErr = 301


def get_error_string(code: ErrorCode) -> str:
    ret = ''
    if code == ErrorCode.LoginFail:
        ret = 'User name or password incorrect'
    elif code == ErrorCode.ParameterErr:
        ret = 'Parameter parse error'

    return ret
