# 001 flask入口文件
# 002 不推荐在入口文件中实例化flask对象 --> ./app/app.py

# 010 导入flask核心对象的生成函数
from app.app import create_app


# 011 创建flask核心对象
app = create_app()
# 014 调用app.run()开启服务器之前，先判断当前文件是否是入口文件


# # 016 定义一个视图函数，通过在普通函数头上加上装饰器绑定路径
# @app.route('/v1/user/get')  # 021 将视图函数转移到对于的文件 .app/api/v1/user.py 中，便于管理
# def get_user():
#     # 017 此函数返回的内容将对应到客户端访问装饰路径的返回上
#     return "我是一只小松鼠~啦啦啦"
#     # 018 由于在#013中我们开启了debug调试模式，更改代码后服务器会自动重启，所以我们可以直接用postman测试此api路由，不需要额外的重启操作
#
#
# # 019 新增第二个视图函数
# @app.route('/v1/book/get')  # 022 将视图函数转移到对于的文件 .app/api/v1/book.py 中，便于管理 --> ./app/api/v1/user.py
# def get_book():
#     return 'get book'
# # 020 发现问题：全部视图函数放在一个文件内，不利于管理，可以依据业务模块划分，将不同的视图函数放到不同的文件当中去


if __name__ == '__main__':
    # 012 调用flask核心对象的run()方法，启动服务器
    app.run(debug=True)  # 013 给定参数debug，并设置为True，打开调试模式
    # 015 通过postman测试
