"""
BMI计算器

Version: 1.0
Author: Gouki

"""

# 获取用户输入的体重，并转换为浮点数
weight = float(input('请输入体重（kg）: '))
# 获取用户输入的身高，并转换为浮点数
height = float(input('请输入身高（m）: '))

# 计算BMI指数，公式为体重除以身高的平方
bmi = weight / height ** 2

# 打印BMI指数，保留一位小数
print(f'{bmi = :.1f}')

# 根据BMI指数，输出不同的健康提示
if 18.5 <= bmi < 24:
    # BMI指数在18.5到24之间，认为是健康体重
    print('你的身材很棒！')
elif bmi < 18.5:
    # BMI指数小于18.5，认为是体重过轻
    print('你的身材太轻啦！')
elif 24 <= bmi < 27:
    # BMI指数在24到27之间，认为是轻微超重
    print('你的身材有一点肥胖！')
elif 27 <= bmi < 30:
    # BMI指数在27到30之间，认为是轻度肥胖
    print('你的身材轻度肥胖啦！')
elif 30 <= bmi < 35:
    # BMI指数在30到35之间，认为是中度肥胖
    print('你的身材中度肥胖啦！')
else:
    # BMI指数大于35，认为是重度肥胖
    print('你的身材重度肥胖啦！')
