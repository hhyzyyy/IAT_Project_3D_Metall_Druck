import matplotlib.pyplot as plt
import numpy as np

plt.ion()
plt.figure(figsize=(4, 4))

# 画单位圆
theta = np.arange(0, 2.1 * np.pi, 2 * np.pi / 100)
plt.plot(np.cos(theta), np.sin(theta))
plt.xlim([-1, 1])
plt.ylim([-1, 1])

# 模拟的随机点数
# n = 100
# a = 2 * np.random.rand(n, 2) - 1
# for i in range(n):
#     color = 'g'
#     if (a[i][0] ** 2 + a[i][1] ** 2) < 1:
#         color = 'r'
#     plt.scatter(a[i][0], a[i][1], c=color, marker='^')
#     plt.pause(0.1)

ax = []
ay = []
plt.ion()
for i in range(10):
    ax.append(i)
    ay.append(i ** 3 + 3 * i + 1)
    plt.plot(ax, ay, 'ro--')
    plt.pause(0.1)
    plt.show()
