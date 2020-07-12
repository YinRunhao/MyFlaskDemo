# -*- coding: utf-8 -*-
import os
from flask import Flask
from flasgger import Swagger

swagger = Swagger()


def init(app: Flask):
    conf_path = os.path.abspath(__file__)
    conf_path = os.path.dirname(conf_path)
    conf_path = os.path.join(conf_path, 'swagger.yml')
    swagger.template_file = conf_path
    swagger.init_app(app)
