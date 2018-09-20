with open('liuhu.txt','r') as read_from,open('liu.txt','w') as write_into:
    content = read_from.read()
    write_into.write(content)