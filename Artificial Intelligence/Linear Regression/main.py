import pandas as pd
import pprint
from sklearn.datasets import fetch_california_housing
from sklearn import linear_model
from sklearn.model_selection import train_test_split

housing = fetch_california_housing()
# pprint.pprint(housing)


df_x = pd.DataFrame(housing.data, columns=housing.feature_names)
df_y = pd.DataFrame(housing.target)

model = linear_model.LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
model.fit(x_train, y_train) #The .fit() method will be used for training the perceptron

result = model.predict(x_test)
print(result[5], y_test)