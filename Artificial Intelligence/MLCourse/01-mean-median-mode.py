# %%
import numpy as np

incomes = np.random.normal(27000, 15000, 10000) # using random.normal creates a random distribution of data (bell curve)
# 27000 is centered data,  15000 is the standard deviation, 10000 is the data points
mean_income = np.mean(incomes) # calculate mean
median_income = np.median(incomes) # calculate median
print(mean_income, median_income)

# %matplotlib inline # this line only works in .ipynb
import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()

new_incomes = np.append(incomes, [1000000000]) # adding an outlier to the data set
new_mean_income = np.mean(new_incomes)
new_median_income = np.median(new_incomes)
print(new_mean_income, new_median_income)

plt.hist(new_incomes, 50)
plt.show()


# generate some fake age data for 500 people:
ages = np.random.randint(18, high=90, size=500)
print(ages)

from scipy import stats
mode_age = stats.mode(ages) # calculate mode
print(mode_age)


# %%
# Exercise: Mean & Median Customer Spend
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
# centered data = 100.0
# std deviation = 20.0
# data points = 10,000

plt.hist(incomes, 50)
plt.show()

mean_income = np.mean(incomes)
median_income = np.median(incomes)
print(mean_income, median_income)