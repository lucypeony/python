#把极域自动在文件名前面的机号前缀去掉
import os
import sys
import re

#遍历当前目录下面的文件
path='./'
for file in os.listdir(path):
	#file can be seen as a string, can use regex on it 
	if re.search('_', file):
		print(file)
	else:
		print("not found")