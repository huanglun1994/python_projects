# -*- coding: utf-8 -*-
"""有理数的加法实现"""
__author__ = 'Huang Lun'

# 用一个python元组表示一个有理数，约定其中的第0项表示分子，第1项表示分母
r1 = (3, 5)
r2 = (7, 10)


def rational_plus(r1, r2):
    """
    有理数的加法定理为：
    r1的分子乘以r2的分母与r1的分母乘以r2的分子之和除以r1与r2的分母之积
    """
    num = (r1[0] * r2[1]) + (r1[1] * r2[0])
    den = r1[1] * r2[1]
    return num, den

print(rational_plus(r1, r2))
