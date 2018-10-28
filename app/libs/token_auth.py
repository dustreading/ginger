# token验证装饰器
from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()  # 此为对象，并非装饰器
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password  # 系统将传入账号和密码
def verify_password(token, password):  # 调用接口，对应的接口函数执行之前，将token传递到这里进行验证
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


# 验证token的函数
def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)  # 如果报错，表明不合法
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    # request 视图函数
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)