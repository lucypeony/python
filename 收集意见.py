'''
文件格式约定：
程序文件：ideas.py

班级名单文件：1班名单；2班名单;……；10班名单.txt
里面的数据格式：
01+一个空格+学生姓名

学生意见存放在文件夹里面：1班文件夹：
里面的格式：01 张三.txt

输出：
1班ideas.txt
1班未交名单.txt

'''
import os
import sys



if __name__ == '__main__':
	className = input("请输入班级，类似1，12：")
	if className:
		#从命令行获得当前班级名称
		print("班级名称是"+className)


		#该班级名单
		classStudentsFile="./"+className+"班名单.txt"
		print("line 27: "+classStudentsFile)
		studentList=list()
		studentF = open(classStudentsFile,encoding="utf-8")
		studentLine = studentF.readline()
		studentList.append(studentLine)
		while studentLine:
			print("line 33: "+studentLine)
			studentList.append(studentLine)
			studentLine=studentF.readline()
		studentF.close()


		#该班级文件夹
		classFolder=className+"班"
		wf=open(classFolder+"ideas.txt",'w')
		homeworkList=list()
		for file in os.listdir(classFolder):
			homeworkList.append(file)
			wf.write(file+"\n")
			print("line 48: "+file)
			#打印出每个文件里的内容
			filef=open(classFolder+"/"+file,encoding="utf-8")
			filefline=filef.readline()
			#print(filefline)
			while filefline:
				print("line 54: "+filefline)
				wf.write(filefline)
				filefline=filef.readline()
			wf.write("\n\n")






		#输出未提交的名单
		nf = open(classFolder+"没交作业.txt",'w')
		for x in studentList:
			print("61: "+x)
			flag= False
			for y in homeworkList:
				print("64:"+y)
				if x[:2]==y[:2]:
					flag=True
					break
			if flag == False:
				print("line 66: "+x)
				nf.write(x+"\n")
			



