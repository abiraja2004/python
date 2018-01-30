import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
x = np.array([0,1,2,3,4,5,6,7,8,9])
x=x.reshape((10,1))
y = np.array([1,3,2,5,7,8,8,9,10,12])
y=y.reshape(10,1)

#splitting the dataset
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)

#adding polynomial features
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(x_train)
regressor = LinearRegression()
regressor.fit(x_poly,y_train)

#visualing the graph
x_grid = np.arange(min(x),max(x),0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(x_train,y_train,color='red')
plt.plot(x_grid,regressor.predict(poly_reg.fit_transform(x_grid)),color='blue')
plt.title('task1')
plt.xlabel('x')
plt.ylabel('y')

x_mean = np.mean(x)
y_mean = np.mean(y)
x2 = 0
x_len = len(x)
for i in range(x_len):
    a=x[i]-x_mean
    b = y[i]-y_mean
    c=a*a
    x2 = x2+(a*b)
print(x2)
b1 = x2/c
print('b1 coefficient : ',b1)
b2 = b-(b1*a)
print('b2 coefficient : ',b2)