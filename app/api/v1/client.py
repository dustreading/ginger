# 069 客户端注册 <-- ./user.py
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint

# 070 实例化红图对象
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')  # 096 将client注册到蓝图中 --> ./__init__.py


# 080 绑定视图函数，多功能注册，实现多种注册方式 --> ../../libs/enums.py
@api.route('/register', methods=['POST'])  # 095 新增资源methods应该为post <-- ../../libs/enums.py
def create_client():
    # 085 注册 登陆 参数 校验 接受 <-- ../../libs/enums.py
    # 086 WTForms 验证表单 --> ../../validators/forms.py
    # 099 将接收到的参数传入ClientForm中进行校验
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL:__register_user_by_email
    }
    promise[form.type.data]()
    return Success()


# 104 邮件注册函数，下一步我们创建用户模型 --> ../../models/user.py
def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)