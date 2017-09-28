# -*- coding: utf-8 -*-
"""有理数类"""
__author__ = 'Huang Lun'


class Rational:
    @staticmethod
    def _gcd(m, n):
        """求最大公约数"""
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n

    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gcd(num, den)
        self._num = sign * (num // g)
        self._den = den // g

    def num(self):
        return self._num

    def den(self):
        return self._den

    def __add__(self, other):
        """加法运算"""


    def print(self):
        print(str(self.num) + '/' + str(self.den))

r1 = Rational(3, 5)
r2 = r1.plus(Rational(7, 15))
r2.print()
