import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["axes.unicode_minus"] = False  # 显示负号

x = np.random.normal(loc=0, scale=1, size=100)
plt.hist(x=x, bins=50)
plt.title("this is a hist figure")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()