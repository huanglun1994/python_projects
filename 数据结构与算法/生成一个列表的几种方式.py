# -*- coding: utf-8 -*-
"""生成一个列表，包含0到10000*（n-1)的整数值"""
__author__ = 'Huang Lun'
import time


def test1(n):
    lst = []
    for i in range(n*10000):
        lst = lst + [i]
    return lst


def test2(n):
    lst = []
    for i in range(n*10000):
        lst.append(i)
    return lst


def test3(n):
    return [i for i in range(n*10000)]


def test4(n):
    return list(range(n*10000))

t1 = time.time()
lst = test3(10)
t2 = time.time()
print(t2 - t1)
t3 = time.time()
lst2 = test4(10)
t4 = time.time()
print(t4 - t3)
