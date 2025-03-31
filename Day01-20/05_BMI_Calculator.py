"""
BMI计算器

Version: 1.0
Author: Gouki

"""
weight = float(input('请输入体重（kg）: '))
height = float(input('请输入身高（m）: '))
bmi = weight / height ** 2
print(f'{bmi = :.1f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
