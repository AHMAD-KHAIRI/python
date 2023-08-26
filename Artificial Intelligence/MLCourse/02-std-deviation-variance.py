# %%
import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)
# centered data = 100.0
# std deviation = 50.0
# data points = 10,000
plt.hist(incomes, 50)
plt.show()

incomes.std()
incomes.var()
# %%
