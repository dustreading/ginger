# 042 自定义的视图管理模块 redprint <-- ./api/v1/book.py


# 043 创建一个Readprint类，先将此类定义为空，后面逐步要将必须的功能添加进去 --> ./api/v1/book.py
class Redprint:
    # 063 依据我们需要的功能，实现红模块的编写 <-- ../api/v1/__init__.py
    def __init__(self, name):  # 064 构造函数，有一个参数name，作为红图的名字
        self.name = name
        self.mound = []
    # 065 模仿蓝图定义route函数

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    # 066 模仿蓝图定义register函数
    def register(self, bp, url_prefix=None):
        # 067 避免冗余，可以在注册的时候不加url_prefix，下一步分析具体用户注册流程 --> ../api/v1/user.py
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
