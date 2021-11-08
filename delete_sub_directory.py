'''

本程序用来给lemon评测去除选手子文件夹

本文件应该放在source文件夹下面，它会把每个选手文件夹里的程序子文件夹里的cpp文件复制粘贴到选手文件夹里面

'''


import os
import shutil


def listdirs(folder):
    return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]


print(os.getcwd())              #打印当前文件夹
print(listdirs(os.getcwd()))    #打印出当前文件夹里的文件


for d in listdirs(os.getcwd()):
    print(d,"student dir")        #打印出选手文件夹名称

    src_path = os.getcwd()+"\\"+d
    out_path = os.getcwd()+"\\"+d

    '''
    
    for f in os.listdir(d):
        
        print(os.getcwd()+"\\"+d+"\\"+f)
    '''
      
    for dirpath, dirnames, filenames in os.walk(src_path):
        for filename in filenames:
            if filename.endswith(".cpp"):
                src = os.path.join(dirpath, filename)
                dest = os.path.join(out_path, filename)
                print("src:",src)
                try:
                    shutil.copy2(src, dest)
                except OSError as err:
                    print(err)
