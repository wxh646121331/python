import numpy as np 
from pandas import DataFrame
import math

# 定义数据和预处理
docA = 'The cat sat on my bed'
docB = 'The dog sat on my knees'

bowA = docA.split(' ')
bowB = docB.split(' ')

# 构建词库
wordSet = set(bowA).union(set(bowB))

# 进行词数统计
wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)

# 遍历文档，统计词数
for word in bowA:
	wordDictA[word] = wordDictA[word] + 1

for word in bowB:
	wordDictB[word] = wordDictB[word] + 1


#print(DataFrame(wordDictA, wordDictB))

# 计算词频TF
def compute_tf(wordDict, bow):
	tf = {}
	nCountBow = len(bow)
	for word in wordDict:
		tf[word] = wordDict[word]/nCountBow
	return tf

tfA = compute_tf(wordDictA, bowA)
print(tfA)
tfB = compute_tf(wordDictB, bowB)
print(tfB)


# 计算逆文档词频IDF
def compute_idf(wordDictList):
	idf = dict.fromkeys(wordDictList[0], 0)
	# 总文档数量
	N = len(wordDictList)
	for wordDict in wordDictList:
		for word, count in wordDict.items():
			if count>0 :
				idf[word] += 1
	for word, count in idf.items():
		idf[word] = math.log10((1+N)/(1 + count))
	return idf

idfs = compute_idf([wordDictA, wordDictB])
print(f'idfs=\n{idfs}')
