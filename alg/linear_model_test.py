from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import numpy as np 

lr = LinearRegression()

# 导入数据
points = np.genfromtxt('data.csv', delimiter=',')
print(f'points:\n{points}')

# 提取points的两列数据，分别作为x,y
x = points[:, 0]
y = points[:, 1]

x_new = x.reshape(-1, 1)
y_new = y.reshape(-1, 1)

lr.fit(x_new, y_new)

# 从训练好的模型中提取系数和截距
w = lr.coef_[0][0]
b = lr.intercept_[0]

print(w, b)

plt.scatter(x, y)
plt.plot(x, w*x+b)
plt.show()
