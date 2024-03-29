#encoding=utf-8

# 基本语法
# 1. Python中严格区分大小写
# 2. 每一行就是一条语句，每条语句以换行结束
# 3. 每条语句不要过长，建议不超过80字符：“rulers":[80],
# 4. 一条语句可以分多行编写，语句后边以\结尾
# 5. Python是缩进严格的语言，所以不要随便写缩进
# 6. 用#号表示注释

print('你好\
,世界')

# 标识符
# 所有可以自主命名的内容都属于标识符
# 比如：变量名、函数名、类名
# 标识符规范：
#   1. 标识符中可以含有字母、数字、_、但是不能以数字开头
#	2. 标识符不能是关键字和保留字，也不建议使用python中的函数名作为标识符，因为这样会导致函数被覆盖
#	3. 命名规范：
#		3.1 下划线命名法：所有字母小写，单词之间使用_隔开：max_length
#		3.2 帕斯卡命名法（大驼峰命名法）：首字母大写，每个单词开头字母大写，其余字母小写：MaxLength



# 数值
# 数值分成3种：整数、浮点数、复数
# 所有的整数都是int类型
# 整数的大小没有限制，可以是一个无限大的整数
a = 999999999999999999 * 999999999
print(a)
b = 999999999999 ** 10 # **表示幂
print(b)
c = 2 ** 2
print(c)
# 如果数字的长度过大，可以使用_作为分隔符 ? 验证未通过
d = 12
print(d)

# 进制
# 十进制的数字不能以0开头
# 其它进制的整数，打印时会以十进制显示
# 二进制 0b开头
# 八进制 0o开头
# 十六进制 0x开头


# 字符串
# 字符串必须用引号括进来
# 单引号和双引号不能跨行使用，如须跨行，需要在行尾使用\
s = '人之初\
性本善'
print(s)
# 三重引号可以换行，并且会保留字符串中的格式：'''、 ”“”
s = '''人之初
性本善'''
print(s)

# 转义字符
# \' 表示 '
# \" 表示 "
# \t 表示制表符
# \n 表示换行符
# \uxxx 表示Unicode编码

# 格式化字符串
# 1. 字符串之间可以进行加法运算
s = 'hello' + ' ' + 'world'
print(s)
# 2. print()函数支持多个参数
print('s=', s)
# 3. 指定占位符
# 	%s 在字符串中表示任意字符
#	%f 浮点数占位符
#	%d 整数占位符
s = 'hello %s'%'wxh'
print(s)
s = 'hello %s, %s'%('wxh', 'tsb')
print(s)
s = 'hello %3.5s'%'abcdefg' # %3.5s 字符串长度限制在3~5之间
print(s)
s = 'hello %s'%1.3435
print(s)
s = 'hello %.2f'%1.43535
print(s)
s = 'hello %d'%1.454
print(s)
# 4. 在字符串前添加一个f来创建一个格式化字符串，可以直接嵌入变量 ?
print(f"t={s}")

# 字符串的复制
s = 'abgagd' * 10
print(s)