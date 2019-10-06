
class person(object) :
	"""
	这是一个文档字符串
	"""

	def __init__(self, name = 'no name'):
		self._name = name
	
	# property装饰器
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name
	
	def sayHello(p):
		print('%s say: "Hello"'%p.name)
		

p1 = person('wxh')
p1.sayHello()
print(p1.name)
p1.name = 'tzl'
p1.sayHello()

p2 = person()
p2.sayHello()

print(type(person))

# help(person)

# 多重继承
print('-'*80)
class a:
	pass
class b:
	pass
class c(a, b):
	pass
print(c.__bases__)


print('_'*80)
# 多态
class aa:
	def __init__(self, name):
		self._name = name;
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name):
		self._name = name

class bb:
	def __init__(self, name):
		self._name = name;
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name):
		self._name = name

o1 = aa('wxh')
o2 = bb('tsb')

def say_hello(obj):
	print('%s say hello'%obj.name)

say_hello(o1)
say_hello(o2)

