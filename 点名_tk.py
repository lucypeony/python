'''
待实现的功能：
点击“点名”按钮后，每隔0.1s输出一行“选择中”
输出50个之后，输出“幸运儿是”

再次点击按钮，清空text()控件

现在的版本不行，只会50*0.1秒之后一起输出
'''
import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import random
import pandas
import time

#新建一个tk窗口
root_window=tk.Tk()
root_window.title('我们要点名啦！')
root_window.geometry('300x400')


name_list=[]

#添加一个文件选择窗口
#excel_file_name是选中的excel文件名，带绝对地址
#print(excel_file_name)
#C:/Users/lucyp/Desktop/Python点名器/测试名单.xlsx
def select_excel_file():
    filetypes =(
        ('excel files','xlsx .xlsx')
    )
    
    filename =fd.askopenfilename(
        title='打开名单excel',
        initialdir='/',
        filetypes=filetypes)


    #显示读入的Excel内容
    #从Excel里读出数据，保存在名单里
    try:
        df=pandas.read_excel(filename)
        global name_list
        name_list=df.values.tolist()
    except:
        tk.messagebox.showwarning(title='Warning',message='Read excel Error!')

    name_list = df.values.tolist()
    #print(name_list)


#open file button
open_button = ttk.Button(
    root_window,
    text='打开excel名单',
    command=select_excel_file
)

open_button.pack(expand=True)



def print_lucky_one():
    cishu=50
    count=0
    for _ in range(cishu):
        name = random.choice(name_list) #学员姓名
        count+=1
        t.insert('1.0', str(count)+"  选择中…… "+ str(name) + "\n")
        #休眠一秒
        time.sleep(0.1)
    t.insert('2.0',"幸运儿是： "+str(name))
        
t = tk.Text()
t.pack()
ttk.Button(root_window, text="点名", command = print_lucky_one).pack()


#run the application
root_window.mainloop()