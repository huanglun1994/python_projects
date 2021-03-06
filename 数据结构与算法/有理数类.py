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

    @staticmethod
    def _verify_type(obj):
        """判断obj是否是有理数对象"""
        if not isinstance(obj, Rational):
            raise TypeError

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
        Rational._verify_type(other)
        den = self._den * other.den()
        num = (self._num * other.den()) + (self._den * other.num())
        return Rational(num, den)

    def __mul__(self, other):
        """乘法运算"""
        Rational._verify_type(other)
        return Rational(self._num * other.num(), self._den * other.den())

    def __floordiv__(self, other):
        """整除运算"""
        Rational._verify_type(other)
        if other.num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * other.den(), self._den * other.num())

    def __sub__(self, other):
        """减法运算"""
        Rational._verify_type(other)
        den = self._den * other.den()
        num = (self._num * other.den()) - (self._den * other.num())
        return Rational(num, den)

    def __truediv__(self, other):
        """除法运算"""
        Rational._verify_type(other)
        if other.num() == 0:
            raise ZeroDivisionError
        return float((self._num * other.den()) / (self._den * other.num()))

    def __eq__(self, other):
        """相等运算"""
        Rational._verify_type(other)
        return self._num * other.den() == self._den * other.num()

    def __lt__(self, other):
        """小于运算"""
        Rational._verify_type(other)
        return self._num * other.den() < self._den * other.num()

    def __gt__(self, other):
        """大于运算"""
        Rational._verify_type(other)
        return self._num * other.den() > self._den * other.num()

    def __ne__(self, other):
        """不等运算"""
        Rational._verify_type(other)
        return self._num * other.den() != self._den * other.num()

    def __le__(self, other):
        """小于等于运算"""
        Rational._verify_type(other)
        return self._num * other.den() <= self._den * other.num()

    def __ge__(self, other):
        """大于等于运算"""
        Rational._verify_type(other)
        return self._num * other.den() >= self._den * other.num()

    def __str__(self):
        return '{0}/{1}'.format(str(self._num), str(self._den))
