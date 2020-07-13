# -*- coding: UTF-8 -*-
from flask import Blueprint, request
from ..models.result import HandleResult
from ..models.errors import ErrorCode
from ..models.logic_models import demo_logic_model as logic_model
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import utility.action_results as action_results

route_demo = Blueprint('api', __name__)


# 路由和对应的方法
@route_demo.route('/', methods=['GET'])
def hello_world():
    """
        测试接口
    """
    result = HandleResult()
    result.msg = 'HelloWorld'
    return action_results.ok(result)


@route_demo.route('/login', methods=['POST'])
def login():
    """
        登录接口
    """
    # 创建请求统一返回类的实例
    result = HandleResult()

    # 获取请求Body中的用户名和密码
    if not request.is_json:
        result.opera_fail(ErrorCode.ParameterErr)
        return action_results.bad_request(result)
    userNm = request.json.get('userNm', None)
    psd = request.json.get('psd', None)

    if userNm is None or psd is None:
        result.opera_fail(ErrorCode.ParameterErr)
        return action_results.bad_request(result)

    # 验证用户并获取用户信息
    result = logic_model.check_user(userNm, psd)
    # 成功则返回OK(200)，并夹带Token
    if result.errorCode == ErrorCode.OK.value:
        # 创建jwt字符串，将用户信息塞到jwt中(实际上可以将任何字典类型塞进jwt中)
        token = create_access_token(identity=result.result.__dict__)
        result.result = token
        return action_results.ok(result)
    # 失败返回400(BadRequset)
    else:
        return action_results.bad_request(result)


@route_demo.route('/info', methods=['GET'])
@jwt_required
def my_info():
    """
        获取Token中记录的用户信息
    """
    usrInfo = get_jwt_identity()
    return action_results.ok(usrInfo)
