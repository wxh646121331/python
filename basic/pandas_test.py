import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from openpyxl.workbook import Workbook
from pandasql import sqldf, load_meat, load_births

# 导入第三方模块：sudo pip3 install pandasql


# Series
print('-'*35+'Series'+'-'*35)
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a','b','c','d'])
print (f'x1:\n{x1}')
print (f'x2:\n{x2}')

d = {'a':1, 'b':2, 'c':3, 'd':4}
x3 = Series(d)
print(x3)

# DataFrame
print('-'*35+'DataFrame'+'-'*35)
data = {'Chinese':[60, 75, 83, 96, 96], 'Math':[79, 90, 94, 98, 98], 'English':[57, 68, 85, 90, 90
], 'sex':['female', 'male', 'male', 'female', None]}
df1 = DataFrame(data)
print(df1)
df2 = DataFrame(data, index=['wxh', 'tsb', 'tzl', 'txy', 'txy'], columns=['Chinese', 'Math', 'English', 'sex'])
default_values = {'Chinese':0, 'sex':'unknown'}
df2.fillna(default_values, inplace=True)
print(df2)

# excel表格
print('-'*35+'xlsx'+'-'*35)
score = DataFrame(pd.read_excel('score.xlsx', index_col=0))
print(score)
df2.to_excel('data.xlsx')

# 删除行或列
print('-'*35+'删除行或列'+'-'*35)
df3 = df2.drop(columns='Math')
print(f'df2:\n{df2}')
print(f'df2:\n{df3}')
df4 = df3.drop(index='wxh')
print(f'df4:\n{df4}')

# 重命名行或列
print('-'*35+'重命名列名'+'-'*35)
df3 = df2.rename(columns={'Chinese':'语文'})
print(f'df2:\n{df2}')
print(f'df3:\n{df3}')

df2.rename(index={'wxh':'wuxinhong'}, inplace=True)
print(f'df2:\n{df2}')

# 去掉重复的行
print('-'*35+'去掉重复的行'+'-'*35)
df3 = df2.drop_duplicates()
print(f'df2:\n{df2}')
print(f'df3:\n{df3}')

# 更改数据格式
print('-'*35+'更改数据格式'+'-'*35)
df2['Chinese'].astype(np.int64)
print(f'df2:\n{df2}')
df2['Chinese'] = df2['Chinese'].astype('str')
print(type(df2['Chinese'][0]))
print(f'df2:\n{df2}')

# 数据间的空格
print('-'*35+'数据间的空格'+'-'*35)
# 删除左右两边空格
df2['Chinese']=df2['Chinese'].map(str.strip)
# 删除左边空格
df2['Chinese']=df2['Chinese'].map(str.lstrip)
# 删除右边空格
df2['Chinese']=df2['Chinese'].map(str.rstrip)
# 删除特殊字符
df2['Chinese']=df2['Chinese'].str.strip('$')
print(f'df2:\n{df2}')

# 大小写转换

print('-'*35+'大小写转换'+'-'*35)
# 全部大写
df2.columns = df2.columns.str.upper()
print(f'df2:\n{df2}')
# 全部小写
df2.columns = df2.columns.str.lower()
print(f'df2:\n{df2}')
# 首字母大写
df2.columns = df2.columns.str.title()
print(f'df2:\n{df2}')
df2.index = df2.index.str.title()
print(f'df2:\n{df2}')
df2['Sex'] = df2['Sex'].str.title()
print(f'df2:\n{df2}')
#df2['Sex'] = df2['Sex'].apply(str.upper)
#print(f'df2:\n{df2}')

# 查找空值
print('-'*35+'查找存在空值的列'+'-'*35)
df3 = df2.isnull().any()
print(df3)

# apply
print('-'*35+'apply'+'-'*35)
def double_df(x):
	return 2*x
df2['Math'] = df2['Math'].apply(double_df)
print(f'df2:\n{df2}')

def plus(df, m, n):
	df['new'] = df['Chinese']*m+df['English']*n
	return df
df2['Chinese'] = df2['Chinese'].astype(np.int64)
df = df2.apply(plus, axis=1, args=[1,2])
print(df)

# 常用的统计函数
print('-'*35+'常用的统计函数'+'-'*35)
# count()统计个数，空值不计算
print(df2.count())
print(df2.count(axis = 1))

# describe():输出多个统计指标
print(df2.describe())
print(df2.min())
print(score.idxmin())
print(score.std())
print(df2.describe(percentiles=[0.9]))

# 数据表合并
print('-'*35+'数据表合并'+'-'*35)
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data':range(5), 'data1':range(0,9,2)})
df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data':range(5), 'data2':range(5)})
print(f'df1:\n{df1}')
print(f'df2:\n{df2}')
df3 = pd.merge(df1, df2, on='name')
print(f'df3:\n{df3}')
# inner是merge的默认连接方式，就是取交集
df3 = pd.merge(df1, df2, how='inner', on=['name', 'data'])
print(f'inner:\n{df3}')

df3 = pd.merge(df1, df2, how='outer')
print(f'outer:\n{df3}')

df3 = pd.merge(df1, df2, how='left')
print(f'left:\n{df3}')
df3 = pd.merge(df1, df2, how='right')
print(f'right:\n{df3}')

# sql的方式打开pandas
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
df = pysqldf(sql)
print(df)
print(type(df))
