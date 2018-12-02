x = 0
print('最外层：', x, id(x))


def outer():
    x = 1
    print('中间层：', x, id(x))

    def inner():
        nonlocal x
        print('已经开始定义nonlocal',x,id(x))
        x = 2
        print("最里层:", x, id(x))

    inner()
    print("outer:", x, id(x))


outer()
print("global:", x, id(x))