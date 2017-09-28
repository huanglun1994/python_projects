# -*- coding: utf-8 -*-
"""类方法维护计数器"""
__author__ = 'Huang Lun'


class Countable:
    counter = 0

    def __init__(self):
        Countable.counter += 1

    @classmethod
    def get_count(cls):
        return Countable.counter

x = Countable()
y = Countable()
z = Countable()
print(Countable.get_count())
