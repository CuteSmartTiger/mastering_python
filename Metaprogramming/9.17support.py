class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        print('----')
        print(clsname,bases,clsdict)
        for name in clsdict:
            print({"clsdic":name})
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self):
        pass

class B(Root):
    def fooar(self):
        pass

# ----
# Root () {'__module__': '__main__', '__qualname__': 'Root'}
# {'clsdic': '__module__'}
# {'clsdic': '__qualname__'}
# ----
# A (<class '__main__.Root'>,) {'__module__': '__main__', '__qualname__': 'A', 'foo_bar': <function A.foo_bar at 0x0000019DBB5B9620>}
# {'clsdic': '__module__'}
# {'clsdic': '__qualname__'}
# {'clsdic': 'foo_bar'}
# ----
# B (<class '__main__.Root'>,) {'__module__': '__main__', '__qualname__': 'B', 'fooar': <function B.fooar at 0x0000019DBB5B9730>}
# {'clsdic': '__module__'}
# {'clsdic': '__qualname__'}
# {'clsdic': 'fooar'}