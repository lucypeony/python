#把极域自动在文件名前面的机号前缀去掉
import os
import sys
import re

#遍历当前目录下面的文件
path='./'
for file in os.listdir(path):
	#file can be seen as a string, can use regex on it 
	if re.search('_', file) and file[0].isdigit():
                dash_index = file.index('_')
                new_name = file[dash_index+1::]    #把文件名里的机号和下换线去掉
                #重命名文件
                #拼接获取绝对路径
                src = os.path.join(os.getcwd(), file)
                dst = os.path.join(os.getcwd(), new_name)

                #使用rename函数
                try:
                        os.rename(src,dst)
                except Exception as e:
                        print(e)
                        print('rename file fail \r\n')
                else:
                        print('rename file succeed\r\n')
                print(file + " " + new_name)
	else:
		print("not found")
