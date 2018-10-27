# 023 来自 ../../../ginger.py 的视图函数的拆分
# 024 刚导入会提示找不到app，这里我们不应该直接导入 ../../app 下的flask核心对象创建函数，会导致循环导入
# 025 我们可以使用蓝图blueprint来注册此路由
# from flask import Blueprint  # 054 删除之，因为我们已经有了红图来管理视图 --> ./book.py

# 026 实例化一个蓝图blueprint
from flask import jsonify

from app.libs.error_code import NotFound
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

# 053 删除此没必须的蓝图，因为蓝图主要作用为模块管理，不因该让其管理视图，视图应该用我们自定义的红图redprint来管理 <-- ./__init__.py
# user = Blueprint('user', __name__)  # 027 第一个参数为此蓝图blueprint的名称，第二个参数为必要的位置信息

# 048 实例化一个redprint，给一个名字为user <-- ./book.py
from app.models.user import User

api = Redprint('user')

# 028 定义好了蓝图之后，我们就不需要flask核心对象了，可以直接用蓝图blueprint来注册视图函数
# @app.route('/v1/user/get')


# 029 使用蓝图user来注册视图函数 --> ./book.py
# @user.route('/v1/user/get')
# 049 改变用红图来注册视图函数，下一步我们需要创建一个蓝图，这是模块界别的蓝图，而红图是视图级别的 --> ./__init__.py
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


# 068 绑定用户注册视图函数 <-- ../../libs/redprint.py
@api.route('/create')
def create_user():
    pass
