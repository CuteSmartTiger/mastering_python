#可以获得文件较多的信息
import fileinput
with fileinput.input('test.txt') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')


with open('test.txt','r') as f:
    for line in f:
        print(f.read(), end='')