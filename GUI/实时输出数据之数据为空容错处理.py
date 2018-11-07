import time
from tkinter import *


def disappear(event):
    root.attributes('-alpha', 0.01)


def show(event):
    root.attributes('-alpha', 1)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    window_wide_center = (screenwidth - width) / 2
    size = '%dx%d+%d+%d' % (width, height, window_wide_center, 0)
    root.geometry(size)


def set_window(root):
    root.attributes('-toolwindow', True, '-alpha', 0.9, '-fullscreen', False, '-topmost', True)
    root.overrideredirect(True)
    root.grid()
    center_window(root, 300, 25)
    root.bind(sequence='<Leave>', func=disappear)
    root.bind(sequence='<Enter>', func=show)


root = Tk()
set_window(root)
var = StringVar()


class CreateContain:

    def __init__(self, root):
        self.fm1_1 = Frame(root)
        Label(text='virtual machine').grid(row=1, column=0, padx=20, pady=2)

        self.fm1_2 = Frame(root)
        Label(textvariable=var, fg='blue', font=("黑体", 12)).grid(row=1, column=1, padx=60, pady=2)

    def get_time(self):
        # time_data=None
        time_data = time.strftime("%H:%M:%S")
        if time_data:
            var.set(time_data)
        else:
            var.set('xxxxx')
        self.fm1_2.after(1000, self.get_time)


if __name__ == '__main__':
    create = CreateContain(root)
    create.get_time()
    mainloop()
