"""
掷骰子6000次，统计每个点出现的次数

Author: Gouki
Version: 1.0

"""

import random


def roll_dice():
    """
    掷骰子
    :return: 骰子点数
    """
    return random.randint(1, 6)


frequency = {i: 0 for i in range(1, 7)}

while True:
    try:
        count_times = int(input("请输入骰子掷几次（正整数）："))
        if count_times > 0:
            break
        else:
            print("请输入一个大于零的整数。")
    except ValueError:
        print("请输入一个有效的正整数。")

for _ in range(count_times):
    result = roll_dice()
    frequency[result] += 1

for key, value in frequency.items():
    print(f"点数{key}出现的次数为{value}")
