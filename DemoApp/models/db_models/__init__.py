# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from ...config import appSetting
import pymysql

db = SQLAlchemy()


def init(app: Flask):
    connStr = ''
    dbType = appSetting.get('BasicSetting', 'DbTypd').upper()
    if dbType == 'MYSQL':
        connStr = appSetting.get('DbConnections', 'MySQL')
        # 使用pymysql作为MySQL的Connector
        pymysql.install_as_MySQLdb()
    elif dbType == 'SQLITE':
        connStr = appSetting.get('DbConnections', 'SQLite')

    app.config['SQLALCHEMY_DATABASE_URI'] = connStr
    db.init_app(app)


class User(db.Model):
    """
        数据库用户表的映射类
    """
    __tablename__ = 'tbUser'
    # 唯一Id
    Id = db.Column('iduser', db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    UserName = db.Column('userName', db.String(16))
    # 密码
    Password = db.Column('psd', db.String(32))
    # 性别
    Sex = db.Column('sex', db.String(8))
    # 所在城市
    City = db.Column('city', db.String(32))
    # 联系电话
    Tel = db.Column('tel', db.String(32))


class Article(db.Model):
    """
        数据库文章表映射类，一个用户
        会有多篇文章
    """
    __tablename__ = 'tbArticle'

    # 唯一ID
    Id = db.Column('idarticle', db.Integer, primary_key=True, autoincrement=True)
    # 标题
    Title = db.Column('title', db.String(64))
    # 内容
    Content = db.Column('content', db.String)
    # 作者ID
    AuthorId = db.Column('author', db.Integer)
