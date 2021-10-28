import os
import sys

#usage: python3 rename.py <path> <str need to replace>


if __name__ == '__main__':
	if len(sys.argv) == 2:
		path ='./'
		old_str = sys.argv[-1]
	elif len(sys.argv) ==3:
		path = sys.argv[1]
		old_str = sys.argv[-1]
	else:
		sys.exit()
	if not path.endswith('/'):
		path = path + '/'

	#遍历目录下面的文件
	for file in os.listdir(path):
		if file.startswith(old_str):
			#替换字符串为空
			name = file.replace(old_str,'')
			#重命名
			os.rename(path+file, path+name)
			print(name)
			pass
print('finish')