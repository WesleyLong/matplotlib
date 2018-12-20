#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : pillar.py
@Author: Wesley
@Date  : 2018/11/26 10:46
@Desc  : 
'''
import numpy as np
import matplotlib.pyplot as plt

# X = [0, 1, 2, 3, 4, 5]
# Y = [222, 42, 455, 664, 454, 334]
# fig = plt.figure()
# plt.bar(X, Y, 0.4, color="green")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("bar chart")
#
# plt.show()

# 设置支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":
    """验证中心极限定理"""
    t = 1000
    a = np.zeros(10000)
    for i in range(t):
        a += np.random.uniform(-5, 5, 10000)
    a /= t
    plt.hist(a, bins=30, color='g', alpha=0.5, normed=True, label='均匀分布叠加')
    plt.legend(loc='upper left')
    plt.grid()
plt.show()
