"""
工资结算
"""

from abc import abstractmethod, ABCMeta

class employee:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass

class manager(employee):
    def __init__(self, name):
        super().__init__(name)
    def get_salary(self):
        return 15000

class programmer(employee):
    def __init__(self, name, work_hour=0):
        super().__init__(name)
        self.work_hour = work_hour
    def get_salary(self):
        return self.work_hour * 200

class sales_man(employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales
    def get_salary(self):
        return 1800 + self.sales * 0.05

emps = [
    manager('王伟'),
    programmer('张三', 100),
    programmer('李四', 150),
    sales_man('王五', 12000),
    sales_man('赵六', 30000),
]
for emp in emps:
    if isinstance(emp, employee):
        ##打印类名
        print (emp.__class__.__name__, emp.name, emp.get_salary())