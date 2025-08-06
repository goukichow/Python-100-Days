import random
import time
from functools import wraps


def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

##函数装饰器
print('*' * 50)


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        ##时间精确到秒并保留一位小数点
        print(f'{func.__name__}耗时: {round(end - start, 1)}秒')
        return result

    return wrapper


download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

##函数装饰器语法糖写法

print('*' * 50)


@record_time
def down(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def up(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


down('MySQL从删库到跑路.avi')
up('Python从入门到住院.pdf')
##去掉函数装饰器的包装
down.__wrapped__('MySQL必知必会.pdf')
up.__wrapped__('Python从新手到大师.pdf')
