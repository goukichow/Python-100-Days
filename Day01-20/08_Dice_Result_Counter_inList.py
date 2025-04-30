"""
将一颗色子掷6000次，统计每种点数出现的次数

Author: 骆昊
Version: 1.1
"""
import random

from openpyxl.styles.builtins import total

counters = [0] * 6
for i in counters:
    print(i)
# 模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
# 输出每种点数出现的次数
total = 0
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')
    total += counters[face - 1]
print(total)