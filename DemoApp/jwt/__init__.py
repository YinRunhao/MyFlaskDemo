# -*- coding: utf-8 -*-
from flask_jwt_extended import JWTManager
from flask import Flask
from ..config import appSetting

jwt = JWTManager()


def init(app: Flask):
    app.config['JWT_SECRET_KEY'] = appSetting.get('BasicSetting', 'JwtSecret')
    jwt.init_app(app)
