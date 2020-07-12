# -*- coding: UTF-8 -*-
class UserDto():
    """
        用户类传输对象，因为业务上可能不需要知道过多的敏感信息
        或者为了简化对象的传输，所以有必要存在专门的传输对象用
        来跟外部接口交互
    """
    def __init__(self):
        # 用户名
        self.UserName = ''
        # 性别
        self.Sex = 'Unknown'
        # 所在城市
        self.City = ''
