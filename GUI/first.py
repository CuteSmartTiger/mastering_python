# import tkinter
# top = tkinter.Tk()
# top.mainloop()

from tkinter import *

# 创建窗口对象的背景色
root = Tk()

# 实现列表
# 创建两个 列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)
for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()
# root.mainloop()  # 进入消息循环


# 实现标签
#创建三个 Label 分别添加到root窗体中
#Label是一种用来显示文字或者图片的组件
Label(root,text = 'pack1',bg = 'red').pack()
Label(root, text = 'pack2', bg = 'blue').pack()
Label(root, text = 'pack3', bg = 'green').pack()

root.mainloop()




