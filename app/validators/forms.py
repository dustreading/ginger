# 087 实现表单的验证 <-- ../api/v1/client.py
from wtforms import StringField, IntegerField, Form
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
    # 088 用户注册所需要的信息
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])  # 090 validators为验证器，用户名为必填字段
    secret = StringField()
    # 089 获取客户端的类型
    type = IntegerField(validators=[DataRequired()])

    # 091 由于系统没有提供type的验证器，我们需要自己实现之
    def validate_type(self, value):
        # 092 将用户传递的值转换为枚举类型，如果转换成功说明有效，不成功则无效
        try:
            client = ClientTypeEnum(value.data)  # 093 value.data才能获取用户传递的真实值
        except ValueError as e:  # 094 捕获到转换失败的错误 --> ../api/v1/client.py
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError
