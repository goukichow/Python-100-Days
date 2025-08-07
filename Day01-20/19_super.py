"""
继承与多态
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

    def eat(self):
        print(self.name, '吃吃吃')

    def sleep(self):
        print(self.name, '睡觉觉')

class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score
    def show(self):
        print(f'{self.name}, {self.age}岁, 分数: {self.score}')
    def eat(self):
        print(self.name,'吃泡面')
    def study(self):
        print(self.name, '正在学习')

class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    def show(self):
        print(f'{self.name}, {self.age}岁, 头衔: {self.title}')
    def teach(self):
        print(self.name, '正在教学')

stu=Student('张三', 18, 90)
techer1=Teacher('王五', 28, '高级讲师')
stu.show()
techer1.show()
stu.eat()
techer1.eat()
stu.sleep()
techer1.sleep()
stu.study()
techer1.teach()
