# encoding=UTF-8
from time import *

st = time()

i = 2
while i<100000:
	flag = True
	j = 2
	while j <= i ** 0.5 :
		if i % j == 0 :
			flag = False
			break
		j = j+1
	if flag :
		print(i)
		pass
	i += 1
et = time()
print("计算耗时：%f"%(et-st))