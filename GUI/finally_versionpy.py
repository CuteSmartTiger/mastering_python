#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: catch_data.py
@time: 2018/11/7 17:26
@desc:
'''
from Tkinter import *
import subprocess
import time

logfile = '/var/log/mtr.log'
file_yaml = '/thinclient_config/vditerminal_config.yaml'

# get ip
def get_ip(file_yaml):
    with open(file_yaml, 'r') as f:
        content = f.readline()
        ip = content.split(':', 1)[1].strip()
    return ip


# ouput data
def output_data(ip, logfile):
    command = r'mtr -4 -n -p {} > {}'.format(ip, logfile)
    px = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = px.pid
    print pid


# check last line
def check_last_line(ip):
    command = r'tail -f -n 1 {}'.format(logfile)
    p_line = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pi = p_line.pid
    print 'pid:'.format(pi)
    return p_line


# 进程只可以调用一次，多次调用不杀死会产生很多进程
# read last line
def read_last_line(p, ip):
    while True:
        content = p.stdout.readline().strip()
        if content:
            if ip in content:
                break
            else:
                continue
        else:
            break
    return content


# deal the data
def deal_the_data(content):
    """
    :param content: str
    :return: net_info,str
    """
    if content:
        split_content = content.split()
        package_loss = split_content[2]
        net_delay = split_content[7]
        nums = split_content[3]
        net_info = 'PACKAGE LOSS:{0}   WOREST NET DELAY:{1}ms'.format(package_loss, net_delay)
    else:
        net_info = 'PACKAGE LOSS:{0}   WOREST NET DELAY:{0}'.format('---')
    print net_info
    return net_info


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
    root.attributes('-alpha', 0.9, '-fullscreen', False, '-topmost', True)
    root.overrideredirect(True)
    root.grid()
    center_window(root, 500, 25)
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
        Label(textvariable=var, fg='blue', font=("黑体", 12)).grid(row=1, column=1, padx=30, pady=2)

    def get_net_info(self):
        content = read_last_line(line, ip)
        net_info_data = deal_the_data(content)
        var.set(net_info_data)
        self.fm1_2.after(1000, self.get_net_info)


if __name__ == '__main__':
    ip = get_ip()
    data = output_data(ip, logfile)
    line = check_last_line(ip)
    create = CreateContain(root)
    create.get_net_info()
    mainloop()
