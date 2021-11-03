'''
可以通过column= row= 来管理控件的布局
'''
from tkinter import *
window = Tk()
window.title("Welcome to my first app")
window.geometry('350x200')



lbl = Label(window,text="your name")
lbl.grid(column=0,row=0)

txt = Entry(window, width=10)
#txt=Entry(window, width=10,state='disabled')
txt.focus()
txt.grid(column=1,row=0)

def clicked():
	res=txt.get()+" you are welcome!"
	lbl.configure(text=res)

btn = Button(window, text="Click me",bg="orange", fg="red", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()