#!/usr/bin/python3
#  -*- coding: utf-8 -*-
import tensorflow as tf

# tf.constant是一个计算，这个计算的结果为一个张量，保存在变量a中。
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = tf.add(a, b, name='add')
print(result)
"""
输出：
Tensor('add:0', shape=(2,), dtype=float32)
"""

# 使用张量记录中间结果
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = a + b

# 直接计算向量的和，这样可读性会比较差
result = tf.constant([1.0, 2.0], name='a') + tf.constant([2.0, 3.0], name='b')
