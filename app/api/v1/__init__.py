# 050 模块级别的蓝图构建 <-- ./user.py

from flask import Blueprint


# 051 创建一个蓝图构造函数
from app.api.v1 import client


def create_blueprint_v1():
    # 056 将红导入 <-- ./book.py
    from app.api.v1 import user, book
    # 052 构造一个v1模块的蓝图，名字就叫v1，模块级别的blueprint已经创建好了，对于视图book和user中的blueprint就没有存在的必要了 --> ./user.py
    bp_v1 = Blueprint('v1', __name__)
    # 057 完成红图到蓝图的注册
    user.api.register(bp_v1)  # 061 加上url_prefix前缀，同时剔除book和user中相应的路由前缀 <-- ../../app.py
    book.api.register(bp_v1)  # 062 假象很完美，下一步我们将要实现红图函数 --> ../../libs/redprint.py
    client.api.register(bp_v1) # 097 将client注册打动蓝图中 --> ./client.py
    # 058 返回蓝图，这时，此时已有红图注册到了蓝图当中，下一步需要将蓝图注册到flask核心对象上去 --> ../../app.py
    return bp_v1
