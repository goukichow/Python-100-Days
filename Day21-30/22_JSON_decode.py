import json

data = {"name": "张三", "age": 30, "city": "北京"}
json_str = json.dumps(data, indent=4)  # 转换为JSON字符串
print(json_str)  # 输出: {"name": "\u5f20\u4e09", "age": 30, "city": "\u5317\u4eac"}
print(type(json_str))  # 输出: <class 'str'>

# JSON 字符串转换为 Python 对象
data = json.loads(json_str)
print(data)
print(type(data))

# 为了让中文字符正常显示，可以使用 ensure_ascii=False 参数
# json_str_chinese = json.dumps(data, indent=4, ensure_ascii=False)
# print(json_str_chinese)  # 输出: {"name": "张三", "age": 30, "city": "北京"}
# print(type(json_str_chinese))