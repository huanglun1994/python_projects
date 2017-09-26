# -*- coding: utf-8 -*-
"""斐波那契数列"""
__author__ = 'Huang Lun'


def fib(n):
    """用递归算法写一个斐波那契数列"""
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib1(n):
    """用递推算法写一个斐波那契数列"""
    f1 = f2 = 1
    for k in range(1, n):
        f1, f2 = f2, f2 + f1
    return f2
