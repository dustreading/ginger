# 003 flask核心对象的初始化和操作
from flask import Flask


# 035 定义蓝图注册函数 <-- ./api/v1/book.py
def register_blueprints(app):  # 036 传入flask核心对象
    # from app.api.v1.user import user  # 037 导入我们先前定义的蓝图
    # from app.api.v1.book import book
    # app.register_blueprint(user)  # 038 调用flask核心对象app的register_blueprint()方法将蓝图注册到其上 --> ./api/v1/book.py
    # app.register_blueprint(book)

    # 059 废弃掉先前的蓝图视图关联，将蓝图红图关联注册到flask核心对象上 <-- ./api/v1/__init__.py
    from app.api.v1 import create_blueprint_v1
    # 060 将蓝图挂载模块前缀url_prefix，去掉book和user中的v1，同时红图也可以模仿之 --> ./api/v1/__init__.py
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    # 004 实例化flask核心对象
    app = Flask(__name__)  # 008 指定flask的位置信息
    # 005 需要将配置文件导入到flask核心对象中 --> ./config/secure.py
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    # 039 调用蓝图注册函数，注册蓝图，用一个单独的函数主要是方便批量注册
    register_blueprints(app)
    # 009 完成flask核心对象的创建，现在将flask核心对象返回 --> ../ginger.py
    register_plugin(app)
    return app
