import tkinter
import time


def gettime():
    # 获取当前时间
    var.set(time.strftime("%H:%M:%S"))
    # 每隔一秒调用函数自身获取时间
    root.after(1000, gettime)


root = tkinter.Tk()
root.title('电子时钟')
var = tkinter.StringVar()
# 设置字体大小颜色
lb = tkinter.Label(root, textvariable=var, fg='blue', font=("黑体", 80))
lb.pack()
gettime()
root.mainloop()
