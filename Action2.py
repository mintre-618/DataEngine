#统计全班成绩
#统计在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差，然后把这些人的总成绩排序，得出名次进行成绩输出。
import numpy as np
personType = np.dtype({
	'names':['姓名', '语文', '数学', '英语'],
	'formats':['U32', 'i', 'i', 'i']})
peoples = np.array([
	("张飞",68,65,30), 
	("关羽",95,76,98), 
	("刘备",98,86,88), 
	("典韦",90,88,77), 
	("许褚",80,90,90)],
	dtype = personType)
#print(peoples)
chColumn = peoples['语文']
maColumn = peoples['数学']
enColumn = peoples['英语']
nameColumn = peoples['姓名']
print("语文的平均成绩为：%f，最小成绩为：%f，最大成绩为：%f，方差为：%f，标准差为：%f 。"
	%(np.mean(chColumn), np.min(chColumn), np.max(chColumn), np.var(chColumn), np.std(chColumn)))
print("数学的平均成绩为：%f，最小成绩为：%f，最大成绩为：%f，方差为：%f，标准差为：%f 。"
	%(np.mean(maColumn), np.min(maColumn), np.max(maColumn), np.var(maColumn), np.std(maColumn)))
print("英语的平均成绩为：%f，最小成绩为：%f，最大成绩为：%f，方差为：%f，标准差为：%f 。"
	%(np.mean(enColumn), np.min(enColumn), np.max(enColumn), np.var(enColumn), np.std(enColumn)))
totalScore = chColumn + maColumn + enColumn
index = np.argsort(-totalScore)
sortName = nameColumn[index]
sortScore = totalScore[index]
#print(totalScore)
#print(index)
#print(sortName)
#print(sortScore)
print("总成绩逆序：", sortScore)
print("排名：", sortName)