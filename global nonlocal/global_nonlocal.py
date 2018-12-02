n = 0

def test():
    global n
    # n += 1
    n = 1
    print(n)


test()
print(n)

def scope_test():
    def do_local():
        spam = "local spam"  # 此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错

    def do_nonlocal():
        nonlocal spam  # 使用外层的spam变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        # print(spam)
        spam = "global spam"

    print('start')
    spam = "test spam"

    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    print('---1----')
    do_global()
    print(spam)
    print('---2----')
    print("After global assignment:", spam)


scope_test()

print('------nnnnn----')

print("In global scope:", spam)
