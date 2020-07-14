# -*- coding: utf-8 -*-
from .. import dto_models
from .. import db_models


def get_user_articles(usrId: int) -> list:
    """
        获取传入用户ID下的所有文章
    """
    ret = []
    lst = db_models.Article.query.filter(db_models.Article.AuthorId == usrId).all()

    for record in lst:
        item = dto_models.ArticleDto()
        item.Title = record.Title
        item.Content = record.Content
        ret.append(item.__dict__)

    return ret
