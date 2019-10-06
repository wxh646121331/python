import pandas as pd
from pandas import Series, DataFrame

print('-'*35+'Series'+'-'*35)
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a','b','c','d'])
print (f'x1:\n{x1}')
print (f'x2:\n{x2}')

d = {'a':1, 'b':2, 'c':3, 'd':4}
x3 = Series(d)
print(x3)

print('-'*35+'DataFrame'+'-'*35)
data = {'Chinese':[60, 75, 83, 96], 'Math':[79, 90, 94, 98], 'English':[57, 68, 85, 90
]}
df1 = DataFrame(data)
print(df1)
df2 = DataFrame(data, index=['wxh', 'tsb', 'tzl', 'txy'], columns=['Chinese', 'Math', 'English'])
print(df2)

print('-'*35+'xlsx'+'-'*35)

