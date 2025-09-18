"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列，并打印结果
a = itertools.permutations('ABCD')
for val in a:
    print(*val)
# 产生ABCDE的五选三组合
b = itertools.combinations('ABCDE', 3)
for val in b:
    print(*val)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
for val in itertools.product('ABCD', '123'):
    print(*val)
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))
