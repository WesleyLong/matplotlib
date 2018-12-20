from scipy import log
import matplotlib.pyplot as plt
import numpy as np
import math

# 设置支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def func(x, a, b):
    return a * log(x) + b


x = np.arange(1, 10, 0.1)
y = log(x)
plt.title("自然对数函数")
plt.plot(x, y)
plt.show()
