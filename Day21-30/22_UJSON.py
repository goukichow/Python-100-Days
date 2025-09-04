import ujson as js

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
file_name = 'udata.json'
with open(file_name, 'w', encoding='utf-8') as file:
    ##不缩进
    js.dump(my_dict, file)
    ##缩进
    js.dump(my_dict, file, indent=4, ensure_ascii=False)
    ##自定义格式
    file.close()

#打印json文件内容，按照python dict的格式
with open(file_name, 'r', encoding='utf-8') as file:
    # my_dict = js.deload(file)
    print(js.dumps(my_dict, indent=4, ensure_ascii=False))
    file.close()