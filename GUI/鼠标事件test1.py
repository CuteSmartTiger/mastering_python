from tkinter import *


class MouseKeyEventDemo:
    def __init__(self):
        # 窗口和标题
        window = Tk()
        window.title("鼠标键盘事件")

        # 打包一个白色画布到窗口
        canvas = Canvas(window, width=200, height=200, bg="white")
        canvas.focus_set()  # 让画布获得焦点
        canvas.pack()

        # 绑定鼠标左键事件，交由processMouseEvent函数去处理，事件对象会作为参数传递给该函数
        canvas.bind(sequence="<button-1>", func=self.processMouseEvent)

        # 绑定鼠标键盘事件，交由processKeyboardEvent函数去处理，事件对象会作为参数传递给该函数
        canvas.bind(sequence="<key>", func=self.processKeyboardEvent)

        # 消息循环
        window.mainloop()

    # 处理鼠标事件，me为控件传递过来的鼠标事件对象
    def processMouseEvent(self, me):
        print("me=", type(me))  # me= <class>

        print("位于屏幕", me.x_root, me.y_root)
        print("位于窗口", me.x, me.y)
        print("位于窗口", me.num)

    # 处理鼠标事件，ke为控件传递过来的键盘事件对象
    def processKeyboardEvent(self, ke):
        print("ke.keysym", ke.keysym)  # 按键别名
        print("ke.char", ke.char)  # 按键对应的字符
        print("ke.keycode", ke.keycode)  # 按键的唯一代码，用于判断按下的是哪个键</class></key></button-1>


MouseKeyEventDemo()
