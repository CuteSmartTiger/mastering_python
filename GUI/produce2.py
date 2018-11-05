import time
from tkinter import *


# 实现的按钮功能
class App:
    def __init__(self, master):
        # 使用Frame增加一层容器
        fm1 = Frame(master)
        # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
        Label(fm1, text='speed').pack(side=TOP, anchor=W, fill=X, expand=YES)
        fm1.pack(side=LEFT, expand=YES, padx=2)

        fm2 = Frame(master)
        Label(fm2, text='2M/s').pack(side=TOP, anchor=W, fill=X, expand=YES)
        fm2.pack(side=LEFT, expand=YES, padx=2)


root = Tk()
root.title("KOYU DATA")
root.geometry("300x150")
display = App(root)
root.mainloop()
