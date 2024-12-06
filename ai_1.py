import pandas as pd
data = pd.read_csv("kalimati_tarkari_dataset.csv")
commodity = data["Commodity"].values
average = data["Average"].values.reshape(-1, 1)
min_price = data["Minimum"].values.reshape(-1,1)
max_price = data["Maximum"].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(average,min_price)
import matplotlib.pyplot as plt
plt.scatter(average, min_price, color = "blue")
plt.plot(average, lin_reg.predict(average), color = 'red')
plt.show()
# plt.scatter(average, max_price, color = "purple")
# plt.show()
# plt.scatter(min_price, max_price, color = "pink")
# plt.show()
