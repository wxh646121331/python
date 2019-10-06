# encoding=utf-8
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1,1]=10
print (a.shape)
print (b.shape)
print (a.dtype)
print (b)

print ('-'*80)

persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})

peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)

ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print (np.mean(ages))
print (np.mean(chineses))
print (np.mean(maths))
print (np.mean(englishs))

print ('-'*80)

animal_type = np.dtype({
	'names':['name', 'color', 'count'],
	'formats':['S32', 'S10', 'i']
	})

animals = np.array([('dog', 'black', 10),('cat', 'white', 20)],
	dtype=animal_type)

names = animals[:]['name']

print(names)

count = animals[:]['count']

print (np.mean(count))

dog = animals[0]

print (dog)

print ('-'*80)

x = np.arange(1,11,2)
print (x)
y = np.linspace(2, 10, 5)
print (y)

print (np.add(x, y))
print (np.subtract(x, y))
print (np.multiply(x, y))
print (np.divide(x, y))
print (np.power(x, y))
print (np.remainder(x, y))
print (np.mod(x, y))

print ('-'*80)
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (np.amin(a))
print (np.amax(a))
print (np.amax(a, 0))
print (np.amax(a, 1))
print (np.amin(a, 0))
print (np.amin(a, 1))
print (np.ptp(a))
print (np.ptp(a, 0))
print (np.ptp(a, 1))
print (np.percentile(a, 90))
print (np.percentile(a, 50, axis=0))
print (np.percentile(a, 50, axis=1))

print (np.median(a))
print (np.median(a, 0))
print (np.median(a, 1))

print ('-'*80)
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print (np.average(a))
# 加权平均值
print (np.average(a, weights=wts))


a = np.array([1,2,3,4])
# 标准差
print (np.std(a))
# 方差
print (np.var(a))


print('-'*30+'排序'+'-'*30)
a = np.array([[4,3,2],[2,4,1]])
print (np.sort(a))
print (np.sort(a, axis=None))
print (np.sort(a, axis=0)) 
print (np.sort(a, axis=1)) 




