import time
from functools import wraps, lru_cache

##斐波那契数列
@lru_cache()
def fibs(n):
    if n in (1, 2):
        return 1
    return fibs(n - 1) + fibs(n - 2)

for i in range(1, 41):
    print(fibs(i))

##递归斐波那契数列
@lru_cache()
def fib1(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
for i in range(1, 11):
    print(fib1(i))