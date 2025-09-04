# import json
#
# my_dict = {
#     'name': '骆昊',
#     'age': 40,
#     'friends': ['王大锤', '白元芳'],
#     'cars': [
#         {'brand': 'BMW', 'max_speed': 240},
#         {'brand': 'Audi', 'max_speed': 280},
#         {'brand': 'Benz', 'max_speed': 280}
#     ]
# }
# print(json.dumps(my_dict))

import json

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
with open('data.json', 'w', encoding='utf-8') as file:
    ##不缩进
    # json.dump(my_dict, file)
    ##缩进
    json.dump(my_dict, file, indent=4, ensure_ascii=False)
    ##自定义格式
    # file.write("{\n")
    # file.write(f"    \"name\": \"{my_dict['name']}\",\n")
    # file.write(f"    \"age\": {my_dict['age']},\n")
    # file.write(f"    \"friends\": {json.dumps(my_dict['friends'], ensure_ascii=False)},\n")
    # file.write("    \"cars\": [\n")
    # for i, car in enumerate(my_dict['cars']):
    #     separator = "," if i < len(my_dict['cars']) - 1 else ""
    #     file.write(f"        {json.dumps(car, ensure_ascii=False)}{separator}\n")
    # file.write("    ]\n")
    # file.write("}\n")
    file.close()

#打印json文件内容，按照python dict的格式
with open('data.json', 'r', encoding='utf-8') as file:
    my_dict = json.load(file)
    print(json.dumps(my_dict, indent=4, ensure_ascii=False))
    file.close()