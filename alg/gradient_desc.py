# 梯度下降法
import numpy as np 
import matplotlib.pyplot as plt 


# 导入数据
points = np.genfromtxt('data.csv', delimiter=',')
print(f'points:\n{points}')

# 提取points的两列数据，分别作为x,y
x = points[:, 0]
y = points[:, 1]

# 用plt画出散点图
# plt.scatter(x, y)
# plt.show()

# 定义损失函数，损失函数是系数的函数，另外还要传入数据的x,y
def compute_cost(w, b, points):
	total_cost = 0
	M = len(points)

	# 逐点计算平方损失误差，然后求平均数据
	for i in range(M):
		x = points[i, 0]
		y = points[i, 1]
		total_cost += (y -w * x - b) ** 2
		return total_cost/M

# 定义超参数
alpha = 0.01
limit = 200
initial_w = 3
initial_b = 1

def fit(points, initial_w, initial_b, alpha, limit):
	w = initial_w
	b = initial_b
	result = []
	for i in range(limit):
		cost = compute_cost(w, b, points)
		w,b = grad_desc(points, w, b, alpha)
		result.append((cost, w, b))

	return result

def grad_desc(points, cur_w, cur_b, alpha):
	M = len(points)
	grad_w = 0
	grad_b = 0
	for i in range(M):
		x = points[i, 0]
		y = points[i, 1]
		grad_w += (cur_w*x+cur_b-y)*x
		grad_b += cur_w*x+cur_b-y
	grad_w = grad_w*2/M
	grad_b = grad_b*2/M
	w = cur_w - alpha * grad_w
	b = cur_b - alpha * grad_b
	return [w, b]

result = fit(points, initial_w, initial_b, alpha, limit)
print(f'result:\n{result}')

result_np = np.array(result)
print(result_np)
#min_cost = np.min(result_np[:, 0])
print(np.min(result_np, 0))
print(np.amin(result_np, 0))
print(result_np.argmin(0))
min_idx = result_np.argmin(0)[0]
min_cost = result_np[min_idx, :]
print(min_cost)
pred_y = min_cost[1]*x + min_cost[2]
cost = result_np[:, 0]
#plt.plot(cost)
plt.scatter(x, y)
#plt.plot(x, pred_y)
#plt.show()

for i in range(len(result_np)):
	pred_y = result_np[i, 1] * x + result_np[i, 2]
	plt.plot(x, pred_y, c = 'r')
plt.show()
