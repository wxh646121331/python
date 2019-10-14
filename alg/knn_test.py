import numpy as np 
from pandas import Series, DataFrame


# 引入sklearn里的数据集： iris
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
#print(li)

# 数据加载和预处理
df = DataFrame(data=iris.data, columns=iris.feature_names)
df['class'] = iris.target
df['class'] = df['class'].map({0:iris.target_names[0], 1:iris.target_names[1], 
	2:iris.target_names[2]})
print(df)
print(df.describe())

x = iris.data
y = iris.target.reshape(-1, 1)

print(x.shape, y.shape)

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, 
	random_state=35, stratify=y)

print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

# 核心算法实现

# 距离函数定义
def l1_distance(a, b):
	return np.sum(np.abs(a-b), axis=1)


def l2_distance(a, b):
	return np.sqrt(np.sum((a-b)**2, axis=1))

distance = l2_distance(x_train, x_test[0].reshape(1, -1))
print(distance)


dist = np.array([3,2,5,1,7,3,4,56,3,6])
nn_index = np.argsort(dist)
nn_y = y_train[nn_index[:6]].ravel()
np.bincount(nn_y)
print(nn_y)


class kNN(object):
	# 定义一个初始化方法，__init__ 是类的构造器
	def __init__(self, n_neighbors = 1, dist_func = l1_distance):
		self.n_neighbors = n_neighbors
		self.dist_func = dist_func

	# 训练模型方法
	def fit(self, x, y):
		self.x_train = x
		self.y_train = y 

	# 模型预测方法
	def predict(self, x):
		# 初始化预测分类数组
		y_pred = np.zeros( (x.shape[0], 1), dtype = self.y_train.dtype )

		# 遍历输入的数据点，取出每一个数据点的序号i和数据x_test
		for i, x_test in enumerate(x):
			# x_test跟所有训练数据计算距离
			distances = self.dist_func(self.x_train, x_test)
			# 得到的距离按照由近到远排序，取出索引值
			nn_index = np.argsort(distances)
			# 选取距离最小的K个点，保存它们对应的分类类别
			nn_y = self.y_train[nn_index[:self.n_neighbors]].ravel()
			# 统计类别中出现频率最高的那个，赋值给y_pred[i]
			y_pred[i] = np.argmax(np.bincount(nn_y))
		return y_pred

# 测试
knn = kNN(n_neighbors = 3, dist_func = l2_distance)
# 训练模型
knn.fit(x_train, y_train)
result_list = []
# 针对不同的参数选取，做预测
for p in [1,2]:
	knn.dist_func = l1_distance if p == 1 else l2_distance
	# 考虑不同的k取值,步长为2
	for k in range(1, 10, 2):
		knn.n_neighbors = k
		# 传入测试数据，做预测
		y_pred = knn.predict(x_test)
		# 求预测准确率
		accuracy = accuracy_score(y_test, y_pred)
		result_list.append([k, 'l1_distance' if p == 1 else 'l2_distance', accuracy])

df = DataFrame(result_list, columns=['k', '距离函数', '预测准确率'])
print(df)

'''
# 传入测试数据，做预测
y_pred = knn.predict(x_test)

print(y_pred)

# 求预测准确率
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
'''
