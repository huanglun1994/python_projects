# -*- coding: utf-8 -*-
"""斐波那契数列"""
__author__ = 'Huang Lun'


def fib(n):
    """用递归算法写一个斐波那契数列"""
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
