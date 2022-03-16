# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["axes.unicode_minus"] = False    # 正常显示图像中的负号

x = np.random.randint(low=2, high=10, size=10)
y = np.random.randint(low=2, high=10, size=10)
plt.scatter(x, y)
plt.title("write your title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.show()
