# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from .models import db_models
from . import log
from . import swagger
from . import jwt
from . import config


def create_app():
    # 生成WebApp
    app = Flask(__name__)
    # 初始化配置模块
    config.init()
    # 跨域
    CORS(app, supports_credentials=True)
    # 初始化数据库映射和链接
    db_models.init(app)
    # 初始化日志组件
    log.init()
    # 注册Controller
    __register_blueprint__(app)
    # 初始化jwt
    jwt.init(app)
    # 初始化Swagger
    swagger.init(app)
    return app


def __register_blueprint__(app: Flask):
    # 引用Controlls里面的蓝图并注册
    from .controllers.DemoController import route_demo
    app.register_blueprint(route_demo, url_prefix='/api')
