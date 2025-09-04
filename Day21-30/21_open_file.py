# if __name__ == "__main__":
#     file = open("致橡树.txt", "r", encoding="utf-8")
#     print(file.read())
#     file.close()
from mailcap import lookup

# file = open("致橡树.txt", "r", encoding="utf-8")
# for line in file:
#     print(line, end="")
# file.close()

# file = open("致橡树.txt", "r", encoding="utf-8")
# lines = file.readlines()
# for i in lines:
#     print(i, end="")
# file.close()

#在文件开始追加，不删除原有内容
# file = open("致橡树.txt", "a+", encoding="utf-8")
# file.write("\n标题： 致橡树")
# file.write("\n作者： 舒婷")
# file.write("\n时间： 1977年3月\n")
# file.close()

try:
    file = open("致橡树d.txt", "r", encoding="utf-8")
    print(file.read())
    file.close()
except Exception as e:
    print(e)
# except FileNotFoundError:
#     print("没有找到文件")
# except UnicodeDecodeError:
#     print("文件编码格式错误")
# except IOError:
#     print("文件读写错误")
# except LookupError:
#     print("文件类型错误")

# file = open("致橡树.txt", "r", encoding="utf-8")
# print(file.read())
# file.close()