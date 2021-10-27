'''
使用Python生成题目测试数据
模板如下，有需要根据它进行更改
'''

import random

fp = open("test1.in",'w') #打开文件
for j in range(1,101): #题目要求输入有多组数据，我这里生成100组
	c = random.randint(1,1001)  #岛屿的数量c-1 
	fp.write(str(c-1)+" "+str(random.randint(99900,100000))+"\n") #生成的随机数转化为字符串之后再写
	for i in range(1,c):
		a = random.randint(-100000,1000000) #横坐标的范围
		b = random.randint(0,100000)        #纵坐标的范围
		fp.write(str(a) + " " + str(b) + "\n")
	fp.write("\n") #每组数据之间有一个换行
fp.write("0 0\n") #输入“0 0”表示结束输入
fp.close();		#关闭文件