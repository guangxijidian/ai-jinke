import matplotlib.pyplot as plt
import numpy as np


# 圆的基本信息
# 1.圆半径
r = 2.0
# 2.圆心坐标
a, b = (0., 0.)
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
plt.plot(x, y)
plt.show()