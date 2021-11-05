'''
把当前目录下的.ans文件重命名为.out文件
'''
import os

for file in os.listdir('.'):
    if file[-3:] =='ans':
        new_name=file[:-3]+"out"
        os.rename(file,new_name)
        print(new_name+"\n")
    
