class Student:
    __slots__='name', 'age',

    def __init__(self, name, age):
        ##初始化属性
        self.name = name
        self.age = age
    # def play(self):
    #     print('student play')

    def play(self):
        print(f'student {self.name} play')

    def study(self, course_name):
        print(f'student {self.name} studying course {course_name}')

stu1 = Student(name='Lily', age=15)
stu2 = Student(name='John', age=13)
print(stu1)
print(stu2)
print(hex(id(stu1)), hex(id(stu2)))
stu1.play()
stu2.study('python')

# 通过“类.方法”调用方法
# 第一个参数是接收消息的对象
# 第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法
# 点前面的对象就是接收消息的对象
# 只需要传入第二个参数课程名称
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

Student.play(stu2)                      # 学生正在玩游戏.
stu2.play()                             # 学生正在玩游戏.