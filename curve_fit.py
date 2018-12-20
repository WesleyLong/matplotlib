import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, math

# 设置支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 一次方程函数
def f_1(x, A, B):
    return A * x + B


# 二次曲线方程
def f_2(x, A, B, C):
    return A * x * x + B * x + C


# 三次曲线方程
def f_3(x, A, B, C, D):
    return A * x * x * x + B * x * x + C * x + D


# 指数曲线方程
def f_4(x, A, B, C):
    return A * np.exp(-B * x) + C


x0 = [0, 0.3, 0.5, 0.8, 1]
y0 = [0.95, 0.82, 0.67, 0.30, 0]

# 描出各点并用直线连接
plt.scatter(x0[:], y0[:], 25, "red")

# 一次曲线拟合
A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
x1 = np.arange(0, 1, 0.01)
y1 = A1 * x1 + B1
plt.plot(x1, y1, "blue", label="一次曲线拟合")
#
# 二次曲线拟合
A2, B2, C2 = optimize.curve_fit(f_2, x0, y0)[0]
x2 = np.arange(0, 1, 0.01)
y2 = A2 * x2 * x2 + B2 * x2 + C2
plt.plot(x2, y2, "green", label="二次曲线拟合")
#
# 三次曲线拟合
A3, B3, C3, D3 = optimize.curve_fit(f_3, x0, y0)[0]
x3 = np.arange(0, 1, 0.01)
y3 = A3 * x3 * x3 * x3 + B3 * x3 * x3 + C3 * x3 + D3
plt.plot(x3, y3, "purple", label="三次曲线拟合")
#
# 指数曲线拟合
A4, B4, C4 = optimize.curve_fit(f_4, x0, y0)[0]
x4 = np.arange(0, 1, 0.01)
y4 = A4 * np.exp(-B4 * x4) + C4
plt.plot(x4, y4, "black", label="指数曲线拟合")

plt.legend()
plt.show()
