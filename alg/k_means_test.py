import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets.samples_generator import make_blobs
# 导入scipy中的距离函数，默认欧式距离
from scipy.spatial.distance import cdist

x, y = make_blobs(n_samples = 100, centers = 6, random_state = 100, cluster_std = 0.6)

'''
plt.figure(figsize = (6, 6))
plt.scatter(x[:, 0], x[:, 1], c = y)
plt.show()
'''

#data = np.array([], dtype = np.float)
#print(data.shape)

class K_Means(object):
	# 初始化参数，分类个数n_cluster，迭代次数max_iter，初始质心centroids
	def __init__(self, n_cluster = 6, max_iter = 300, centroids = []):
		self.n_cluster = n_cluster
		self.max_iter = max_iter
		self.centroids = np.array(centroids, dtype = np.float)

	# 训练模型方法，k-means聚类过程
	def fit(self, data):
		# 若没有指定初始质心，随机选取data中的点作为初始质心
		if (self.centroids.shape == (0,) ):
			# 从data中随机生成0到data行数的6个整数，作为索引值
			self.centroids = data[ np.random.randint(0, data.shape[0], self.n_cluster) , :]

		# 开始迭代
		for i in range(self.max_iter):
			# 1.计算距离矩阵，得到一个100*6的矩阵
			distances = cdist(data, self.centroids)

			# 2.对距离由近到远排序，选取最近的质心点的类别，作为当前点的分类
			c_ind = np.argmin( distances, axis = 1)

			# 3.对每一类型进行均值计算，更新质心点坐标
			for i in range(self.n_cluster):
				for i in c_ind:
					#选出所有类型是i的点，取data里面坐标的均值，更新第i个质心
					self.centroids[i] = np.mean(data[c_ind == i], axis = 0)

	# 实现预测方法
	def predict(self, samples):
		distances = cdist(samples, self.centroids)
		c_ind = np.argmin(distances, axis = 1)
		return c_ind

def plotKMeans(x, y, centroids, subplot, title):
	# 分配子图，121表示一个1行两列的子图的第一个
	plt.subplot(subplot)
	plt.scatter(x[:, 0], x[:, 1], c = 'r')
	# 画出质心点
	plt.scatter(centroids[:, 0], centroids[:, 1], c = np.array(range(6)), s = 100)
	plt.title = title

# 测试
centroids = np.array([[-10, -5],[-5, 0],[0, -5],[-2, 10],[5, 5],[10, 0]])
#centroids = x[ np.random.randint(0, x.shape[0], 6) , :]
k_means = K_Means(centroids = centroids)
plt.figure(figsize = (16, 6))
plotKMeans(x, y, k_means.centroids, 221, "initail")
k_means.fit(x)
plotKMeans(x, y, k_means.centroids, 222, "final")
#plt.show()

plt.subplot(223)
plt.scatter(x[:, 0], x[:, 1], c = y)

y_pred = k_means.predict(x)
plt.subplot(224)
plt.scatter(x[:, 0], x[:, 1], c = y_pred)
plt.show()