import time
#数据结构与算法python实现
class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls,*args,**kwargs)
        return cls._instance
class Singleton2(object):
    instance = {}
    def getinstance():
        if cls not in instance:
            instances[cls] = cls(*args,**kwargs)
        return instance[cls]

