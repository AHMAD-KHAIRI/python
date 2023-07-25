import matplotlib.pyplot as plt # for plotting

import pandas as pd # for data handling
import numpy as np # for calculations

import scipy
import scipy.stats as st # for statistical calculations

from scipy.stats import norm # normal distribution

# expected values
mu1 = 0
mu2 = -1
mu3 = 2

# standard deviations (=sigma)
std1 = 1
std2 = 0.5
std3 = 5

# x axis
x = np.arange(-5, 5, 0.1)

# generate distributions for varying expected value mu
y1 = norm.pdf(x, mu1, std1)
y2 = norm.pdf(x, mu2, std1)
y3 = norm.pdf(x, mu3, std1)

# plot
plt.rcParams["figure.figsize"] = (15, 5)
plt.subplot(1, 2, 1)
plt.plot(x, y1, label=r"$\mu = 0$")
plt.plot(x, y2, label=r"$\mu = -1$")
plt.plot(x, y3, label=r"$\mu = 2$")
plt.legend(fontsize= 15)
plt.xlabel(r"$x$", fontsize= 15)
plt.ylabel(r"$f(x|\mu, 1)$", fontsize= 15)

# generate distributions for varying variance sigma
y1 = norm.pdf(x, mu1, std1)
y2 = norm.pdf(x, mu1, std2)
y3 = norm.pdf(x, mu1, std3)

# plot
plt.subplot(1, 2, 2)
plt.plot(x, y1, label=r"$\sigma = 1$")
plt.plot(x, y2, label=r"$\sigma = 0.5$")
plt.plot(x, y3, label=r"$\sigma = 5$")
plt.legend(fontsize= 15)
plt.xlabel(r"$x$", fontsize= 15)
plt.ylabel(r"$f(x|0,\sigma)$", fontsize=15)
plt.show()

# We can see that:
# - increasing mu shifts the curve to the right (decreasing mu shifts the curve to the left).
# - increasing sigma flattens the curve (decreasing sigma amplifies the curve)