# -*- coding: utf-8 -*-
"""有理数的加法实现"""
__author__ = 'Huang Lun'

# 一个有理数3/5的存储方式如下
a1 = 3
b1 = 5


def rational_plus(a1, b1, a2, b2):
    """
    有理数的加法定理为：
    (a1*b2+b1*a2)/(b1*b2)
    """
    num = (a1 * b2) + (b1 * a2)
    den = b1 * b2
    return num, den

print(rational_plus(a1, b1, 7, 10))
