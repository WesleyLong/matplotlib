#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : pyplot.py
@Author: Wesley
@Date  : 2018/11/26 10:21
@Desc  : 
'''
import math

import matplotlib.pyplot as plt
import numpy as np

# 设置支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# x = np.arange(0, 10, 0.1)
# y = x * 2
# plt.title("一元一次函数")
# plt.plot(x, y)

# x = np.arange(-10, 10, 0.1)
# y = x ** 2 + 2 * x + 1
# plt.title("一元二次函数")
# plt.plot(x, y)
#
# x = np.arange(0, 10, 0.1)
# y = 2 ** x
# plt.title("指数函数")
# plt.plot(x, y)
#
x = np.arange(1, 100, 1)
y = [math.log(a, math.e) for a in x]
plt.title("自然对数函数")
plt.plot(x, y)
#
# x = np.linspace(-np.pi, np.pi, 100)
# y = np.sin(x)
# plt.title("正弦函数")
# plt.plot(x, y)

plt.show()
