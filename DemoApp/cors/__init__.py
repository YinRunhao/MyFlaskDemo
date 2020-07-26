# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS


def init(app: Flask):
    # 对全局路由跨域
    CORS(app)
    # 只对某些路由跨域
    # CORS(app, resources={r"/api/*": {"origins": "*"}})
