# 006 存放api敏感配置项 -> ./setting.py

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root@localhost/ginger'

SECRET_KEY = 'abvc'

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_COMMIT_TEARDOWN = True
