# -*- coding: utf-8 -*-
"""求任意正实数的平方根"""
__author__ = 'Huang Lun'
import math


def sqrt1(num):
    """
    牛顿迭代法：
    0.对给定正实数x和允许误差e，令变量y取任意正实数值，如令y=x；
    1.如果y*y与x足够接近，即丨y*y-x丨<e，计算结束并把y作为结果；
    2.取z=（y+x/y）/2；
    3.将z作为y的新值，回到步骤1。
    """
    y = 1.0
    while abs(y * y - num) > 1e-6:
        y = (y + num/y) / 2
    return y


def sqrt2(num):
    """
     二分法：
     求根号5
     a:折半：       5/2=2.5
     b:平方校验:  2.5*2.5=6.25>5，并且得到当前上限2.5
     c:再次向下折半:2.5/2=1.25
     d:平方校验：1.25*1.25=1.5625<5,得到当前下限1.25
     e:再次折半:2.5-(2.5-1.25)/2=1.875
     f:平方校验：1.875*1.875=3.515625<5,得到当前下限1.875
    """
    x = math.sqrt(num)
    y = num / 2.0
    low = 0.0
    up = num * 1.0
    count = 1
    while abs(y - x) > 1e-8:
        print(count, y)
        count += 1
        if (y * y) > num:
            up = y
            y = low + ((y - low) / 2)
        else:
            low = y
            y = up - ((up - y) / 2)
    return y
