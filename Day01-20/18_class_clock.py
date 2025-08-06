'''
定义一个类描述数字时钟，提供走字和显示时间的功能
'''

import time

'''
数字时钟类，用于模拟数字时钟的运行和显示
'''
class Clock:
    '''
    初始化时钟对象

    Args:
        seconds (int): 秒数，默认为0
        minutes (int): 分钟数，默认为0
        hours (int): 小时数，默认为0
    '''
    def __init__(self, seconds=0, minutes=0, hours=0):
        self.sec = seconds
        self.min = minutes
        self.hour = hours

    '''
    时钟走字功能，每调用一次秒数加1，并处理进位逻辑
    '''
    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    '''
    显示当前时间，格式为HH:MM:SS
    
    Returns:
        str: 格式化后的时间字符串
    '''
    def show(self):
        return '%02d:%02d:%02d' % (self.hour, self.min, self.sec)

# 创建时钟对象，初始时间为23:59:56
clock1 = Clock(56, 59, 23)
# 循环显示时间和更新时钟
while True:
    print(clock1.show())
    time.sleep(1)
    clock1.run()
