"""
定义一个类描述平面上的点，提供计算到另一个点距离的方法
"""

class Point:
    """
    平面上的点类

    Attributes:
        x (float): 点的x坐标
        y (float): 点的y坐标
    """

    def __init__(self, x, y):
        """
        初始化点对象

        Args:
            x (float): 点的x坐标
            y (float): 点的y坐标
        """
        self.x = x
        self.y = y

    def distance(self, another_point):
        """
        计算当前点到另一个点的欧几里得距离

        Args:
            another_point (Point): 另一个点对象

        Returns:
            float: 当前点到另一个点的距离
        """
        return (abs((self.x - another_point.x)) ** 2 + abs((self.y - another_point.y)) ** 2) ** 0.5

    def __str__(self):
        """
        返回点的字符串表示形式

        Returns:
            str: 点的坐标字符串，格式为"(x, y)"
        """
        return f'({self.x}, {self.y})'

# 创建两个点对象并测试距离计算功能
p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1)
print(p2)
print(p1.distance(p2))
