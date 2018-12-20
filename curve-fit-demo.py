import matplotlib.pyplot as plt
import numpy as np

# 设置支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(-np.pi, np.pi, 100)

y = np.sin(x)

plt.title("正弦函数")
plt.plot(x, y)
plt.show()
