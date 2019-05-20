import numpy as np


def my_fit(x, y, power):
    size = len(x)
    c = np.ones((1, size))
    x_arr = np.array(x)
    x_a = x_arr.copy()
    x_a.resize((1, size))
    x_mat = np.append(x_a, c, axis=0)
    y_arr = np.array(y)
    y_arr.resize((1, size))
    y_mat = np.mat(y_arr)
    for i in range(2, power + 1):
        temp_x = x_arr ** i
        temp_x.resize((1, size))
        x_mat = np.append(temp_x, x_mat, axis=0)
    x_mat = np.mat(x_mat)
    w = (x_mat * x_mat.T).I * x_mat * y_mat.T
    w0 = w.T
    w0.resize(w0.size)
    return w0


def f(x):
    return 2 * x ** 2 + x + 3


x = np.linspace(-5, 5)
y = f(x) + 0.5 * np.random.randn(len(x))  # 加入噪音
y_fit = np.polyfit(x, y, 2)  # 二次多项式拟合
print(y_fit)
w = my_fit(x, y, 2)
print(w)
