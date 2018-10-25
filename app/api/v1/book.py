# 030 来自 ../../../ginger.py 的视图函数的拆分

# 031 同样地，我们不需要使用flask核心对象来注册路由，而是用蓝图blueprint
# @app.route('/v1/book/get')

# from flask import Blueprint # 055 同理，我们把你放到了更高的岗位，拜拜！之后呢？视图将由红图redprint来统一管理，并将红图redprint注册到蓝图blueprint之上 --> ./__init__.py
from app.libs.redprint import Redprint

# 032 定义一个蓝图，名称为book，并指定当前路径
# book = Blueprint('book', __name__)  # 054 很抱歉兄弟，大材小用了，你是模块级别的，这个视图级别应该让小人来做 <-- ./user.py

# 044 实例化一个Redprint <-- ../../libs/redprint.py
api = Redprint('book')


# 033 将路由/视图函数注册到蓝图上
# @book.route('/v1/book/get')  # 045 我们定义了专门管理视图的模块redprint所以不需要用模块管理工具blueprint来注册视图函数
# 046 使用redprint来注册视图函数
@api.route('/get')
def get_book():
    return '苏菲的世界'

# 034 现在两个蓝图已经注册好了，但是怎么样才能让蓝图生效呢？将蓝图注册到flask核心对象上即可！ --> ../../app.py


# 039 蓝图是作为模块级别的划分，不应该只局限于视图 <-- ../../app.py
# 040 我们再添加一个视图
# @book.route('/v1/book/create')  # 041 这里，我们发现路由中 /v1/book/ 和上一个路由重复了，避免冗余，这个问题应该得到解决 --> ../../libs/redprint.py
# 047 这里同样也要改变一下，用红图来注册 --> ./user.py
@api.route('/create')
def create_book():
    return 'create book'
