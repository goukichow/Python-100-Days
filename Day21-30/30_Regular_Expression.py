import re

userName = input("Please input your name: ")
if not re.match(r'^[0-9a-zA-Z_]{6,20}$', userName):
    print("Invalid username!")
    userName = input("Please input your name: ")

qq = input("Please input your QQ number: ")
if not re.fullmatch(r'[1-9][0-9]{4,11}', qq):
    print("Invalid QQ number!")
    qq = input("Please input your QQ number: ")

print("Your name is %s, your QQ number is %s" % (userName, qq))

# 匹配手机号
# 创建正则表达式对象，使用了前瞻和回顾来保证手机号前后不应该再出现数字
pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''
# 方法一：查找所有匹配并保存到一个列表中
tels_list = re.findall(pattern, sentence)
for tel in tels_list:
    print(tel)
print('--------华丽的分隔线--------')

# 方法二：通过迭代器取出匹配对象并获得匹配的内容
for temp in pattern.finditer(sentence):
    print(temp.group())
print('--------华丽的分隔线--------')

# 方法三：通过search函数指定搜索位置找出所有匹配
m = pattern.search(sentence)
while m:
    print(m.group())
    m = pattern.search(sentence, m.end())

# 替换匹配项
sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'
pulified = re.sub(r'[sS]hit|[Ff]uck|[啥傻沙][比逼币笔缺叉吊屌雕]', '*%$#', sentence)
print(pulified)

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。]', poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)