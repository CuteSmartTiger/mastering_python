import time
from tkinter import *

root = Tk()
root.title("KOYU DATA")
root.geometry("300x150")

# 使用Frame增加一层容器
fm1_1 = Frame(root)
Label(fm1_1, text='speed').pack(side=TOP, anchor=W, fill=X, expand=YES)
fm1_1.pack(side=LEFT, expand=YES, padx=2)

fm1_2 = Frame(root)
var = StringVar()
Label(fm1_2, textvariable=var, fg='blue', font=("黑体", 12)).pack(side=TOP, anchor=W, fill=X, expand=YES)
fm1_2.pack(side=LEFT, expand=YES, padx=2)

fm2_1 = Frame(root)
Label(fm2_1, text='speed').pack(side=TOP, anchor=W, fill=X, expand=YES)
fm2_1.pack(side=BOTTOM, expand=YES, padx=2)

fm2_2 = Frame(root)
var2 = StringVar()
Label(fm2_2, textvariable=var2, fg='blue', font=("黑体", 12)).pack(side=TOP, anchor=W, fill=X, expand=YES)
fm2_2.pack(side=BOTTOM, expand=YES, padx=2)


def gettime1():
    # 获取当前时间
    var.set(time.strftime("%H:%M:%S"))
    # 每隔一秒调用函数自身获取时间
    fm1_2.after(1000, gettime1)


def gettime2():
    # 获取当前时间
    var2.set(time.strftime("%H:%M:%S"))
    # 每隔一秒调用函数自身获取时间
    fm2_2.after(1000, gettime2)


gettime1()
gettime2()
root.mainloop()
