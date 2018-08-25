# 9.23. Executing Code with Local Side Effects

def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    return b

print(test())

def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x =', x)
    return loc,loc['x']

print(test2())
# before: {'x': 0}
# after: {'x': 1, 'loc': {...}}
# x = 0
# ({'x': 1, 'loc': {...}}, 1)