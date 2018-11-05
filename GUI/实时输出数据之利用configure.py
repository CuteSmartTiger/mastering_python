# 方法一：利用configure()或config()方法实现文本变化
import tkinter
import time


def gettime():
    # 获取当前时间并转为字符串
    timestr = time.strftime("%H:%M:%S")
    # 重新设置标签文本
    lb.configure(text=timestr)
    # 每隔一秒调用函数gettime自身获取时间
    root.after(1000, gettime)


root = tkinter.Tk()
root.title('电子时钟')
# 设置字体大小颜色
lb = tkinter.Label(root, text='', fg='blue', font=("黑体", 80))
lb.pack()
gettime()
root.mainloop()
