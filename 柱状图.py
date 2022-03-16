import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["axes.unicode_minus"] = False  # 显示负号

x = ["a", "b", "c", "d"]
y = [1, 3, 5, 7]
plt.bar(x, y, width=0.5)
plt.title("this is a bar figure")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()