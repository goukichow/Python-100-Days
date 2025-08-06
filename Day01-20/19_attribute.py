class Student:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def study(self, course_name):
        print(f'{self._name}正在学习{course_name}.')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
print(stu._name)  # AttributeError: 'Student' object has no attribute '__name'
print(stu._age)