class InputError(ValueError):
    """
    Raises an InputError with the given message.
    """
    pass

def fac( num):
    #求阶乘
    if num < 0:
        raise InputError('只能计算非负数整数的阶乘')
    if num in (0,1):
        return 1
    else:
        return num * fac(num - 1)

flag = True
while flag:
    num = int(input("请输入一个正整数："))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False
    except Exception as err:
        print(err)