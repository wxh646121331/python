#incoding=UTF-8
# type() 用来检查对象的类型
a = 4890354676879876787989
b = '123'
print(type(a))
print(type(b))

# id() 用来获取对象的地址
print(id(a))
print(id(b))

c = 4890354676879876787989
print(id(c))

# 对象的结构
# id : CPython中id就是对象的内存地址，对象一旦创建，则不能更新
# type : 对象的类型，对象一旦创建，则不能更新
# value

# 类型转换
# int()、str()、float()、bool()

# 算术运算符
# +
# -
# *
# /
# // 整除
# **
# %


# 逻辑运算符
# not
# and
# or

# 条件运算符（三元运算符）
# 语法：语句1 if 条件表达式 else 语句2


# 代码块
# 以缩进开始，直到代码恢复到之前的缩进级别时结束

# input()函数
# 用来获取用户输入，返回值是str
i = input('请输入一个数字: \n')
print('输入内容：%s'%i)


# 命名空间
scope = locals()
print(scope)

def my_function():
	scope = locals()
	glob = globals()
	print(scope)
	print(glob)

my_function()
