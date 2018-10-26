# 081 实现各种各样的枚举 <-- ../api/v1/client.py
from enum import Enum


# 082 用不同的Enum来对应不同的用户的登陆方式
class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    USER_MINA = 200  # 083 微信小程序
    USER_WX = 201  # 084 微信公众号 --> ../api/v1/client.py
