# -*- coding: utf-8 -*-
from .. import dto_models
from .. import db_models


def get_user_info(usrNm: str, psd: str) -> dto_models.UserDto:
    """
        获取用户信息，失败返回None
    """
    dto = None
    dbUsr = db_models.User.query.filter(db_models.User.UserName == usrNm).first()
    if dbUsr is not None:
        if dbUsr.Password == psd:
            dto = dto_models.UserDto()
            dto.City = dbUsr.City
            dto.Sex = dbUsr.Sex
            dto.UserName = dbUsr.UserName
    return dto


def get_user_id(usrNm: str) -> int:
    """
        以用户名获取用户ID, 找不到返回-1
    """
    ret = -1
    dbUsr = db_models.User.query.filter(db_models.User.UserName == usrNm).first()
    if dbUsr is not None:
        ret = dbUsr.Id
    return ret
