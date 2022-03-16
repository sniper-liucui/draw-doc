import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["axes.unicode_minus"] = False  # 显示负号

x = np.linspace(start=-30, stop=30, num=1000)
y = np.sin(x)
plt.plot(x, y)
plt.title("y = sin(x)")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()