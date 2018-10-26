# 069 客户端注册 <-- ./user.py
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError
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

    # 098 接收客户端传过来的参数 <-- ./__init__.py
    data = request.json
    # 099 将接收到的参数传入ClientForm中进行校验
    form = ClientForm(data=data)  # 100 用json的方式接收数据，需使用data关键字参数进行传入
    # 101 调用form的validate方法进行校验，如果校验通过，我们就可以进行后续的操作
    if form.validate():  # 102 不同的客户端的注册代码是不同的，想办法实现应对不同客户端的处理函数
        # 103 用一个字典，实现客户端与处理函数之间的对应关系
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email
        }
        promise[form.type.data]()
    else:
        raise ClientTypeError()
    return 'success'


# 104 邮件注册函数，下一步我们创建用户模型 --> ../../models/user.py
def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)