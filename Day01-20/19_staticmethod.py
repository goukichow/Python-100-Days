class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod   # 静态方法
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# 调用静态方法，无需实例化
print(Triangle.is_valid(3, 4, 5))
t = Triangle(3, 4, 5)
#通过属性访问周长
print(f'周长: {t.perimeter}')
#通过属性访问面积
print(f'面积: {t.area}')
#通过方法访问面积
# print(f'面积: {t.area()}')
