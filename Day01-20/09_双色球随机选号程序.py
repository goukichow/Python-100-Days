"""
双色球随机选号程序

Author:vGouki Chow
Version: 1.0
"""
import random

# nums = int(input('请输入要生成的组数：'))
nums=5
for _ in range(nums):
    redBall = list(range(1, 34))
    selectBalls = []

    for _ in range(6):
        index = random.randrange(len(redBall))
        selectBalls.append(redBall.pop(index))

    selectBalls.sort()
    # print(f"\033[031m{selectBalls}\033[0m\t\t", end=' ')

    print(f"\033[031m{' '.join(f'{num:>3}' for num in selectBalls)}\033[0m", end=' ')

    blueBall = random.randrange(1, 17)

    # print(f"\t+\t\033[032m{blueBall}\033[0m")
    print(f"\033[032m{blueBall:>3}\033[0m")

