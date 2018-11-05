import tkinter as tk
from tkinter import ttk


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d-%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)


root = tk.Tk()
root.title('测试窗口')
print(get_screen_size(root))
print(get_window_size(root))
center_window(root, 300, 240)
root.maxsize(600, 400)
root.minsize(300, 240)
ttk.Label(root, relief=tk.FLAT, text='屏幕大小(%sx%s)\n窗口大小(%sx%s)' % (get_screen_size(root) + get_window_size(root))).pack(
    expand=tk.YES)
tk.mainloop()
