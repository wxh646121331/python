#incoding=UTF-8
def add(*a):
	"""
 	这是一个文档字符串
	"""
	result =0
	for i in a :
		result += i
	return result

res = add(1,2,3)
print(res)


help(add)


# 装饰器
def decoretor(original):
	def inner(*args, **keyargs):
		print('-'*20)
		r = original(*args, **keyargs)
		print('-'*20)
		return r
	return inner

new_add = decoretor(add)
print(new_add(343,546,666))


# 匿名函数
list = [1,2,3,4,5]