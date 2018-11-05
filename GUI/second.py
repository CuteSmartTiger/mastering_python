from tkinter import *


class MyApp(object):

    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Frame(parent)
        self.frame.pack()

        btn = Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()

    def hide(self):
        self.root.withdraw()

    def openFrame(self):
        self.hide()
        otherFrame = Toplevel()
        otherFrame.geometry("400x300")
        otherFrame.title("otherFrame")
        handler = lambda: self.OnCloseOtherFrame(otherFrame)
        btn = Button(otherFrame, text="Close", command=handler)
        btn.pack()

    def OnCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

    def show(self):
        self.root.update()
        #将其隐藏
        # self.root.iconify()
        # 将隐藏的显示出来
        self.root.deiconify()


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()
    root.withdraw()
