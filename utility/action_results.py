# -*- coding: UTF-8 -*-
from flask import Response
from . import MyEncoder, json


def __to_json__(obj) -> str:
    """ 制作json字符串

    根据传入对象制作

    Arg:
        body: 回送字符串
        status_code: 状态码

    return:
        Http回送
    """
    jsonStr = ''
    if isinstance(obj, str):
        jsonStr = obj
    elif isinstance(obj, dict):
        jsonStr = json.dumps(obj, cls=MyEncoder, ensure_ascii=False)
    else:
        dic = obj.__dict__
        jsonStr = json.dumps(dic, cls=MyEncoder, ensure_ascii=False)
    return jsonStr


def __make_response__(body: str, status_code: int):
    """ 制作Http回送

    根据传入的body字符串和状态码制作http回送

    Arg:
        body: 回送字符串
        status_code: 状态码

    return:
        Http回送
    """
    resp = Response(body.encode('utf8'),
                    status=status_code,
                    mimetype='application/json')
    return resp


def ok(obj) -> Response:
    """200
    """
    jsonStr = __to_json__(obj)
    resp = __make_response__(jsonStr, 200)
    return resp


def not_found(obj) -> Response:
    """404
    """
    jsonStr = __to_json__(obj)
    resp = __make_response__(jsonStr, 404)
    return resp


def created(url: str, obj) -> Response:
    """201
    """
    jsonStr = __to_json__(obj)
    resp = __make_response__(jsonStr, 201)
    resp.headers['Location'] = url
    return resp


def bad_request(obj) -> Response:
    """400
    """
    jsonStr = __to_json__(obj)
    resp = __make_response__(jsonStr, 400)
    return resp


def no_content() -> Response:
    """204
    """
    resp = Response(status=204)
    return resp


def unauthorized() -> Response:
    """401
    """
    resp = Response(status=401)
    resp.headers['WWW-Authenticate'] = 'Basic'
    return resp
