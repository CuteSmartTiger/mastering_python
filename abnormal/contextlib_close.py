print('-------------contextlib.closing-----------')
# 方法三：
# 先看一个简单的事例
class test:
    def start(self):
        print('start')
    def close(self):
        print('end')
    def __enter__(self):
        print('biaoji')
        # 进入时调用当前实例本身
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('dingwei')
        # 退出时调用close方法
        self.close()

with test() as test_obj:
    test_obj.start()


# 运行机理： with通过__enter___方法将test()打开进入上下文管理，返回实例self记为test_obj，
# 然后调用实例的方法test_obj.start()，然后通过__exit__退出上下文管理器，调用self.close()方法
# 输出结果如下：
# biaoji
# start
# dingwei
# end

print('----------youhua-----------')
# 对以上方法的优化
import contextlib
class test:
    def start(self):
        print('start')
    def close(self):
        print('end')

with contextlib.closing(test()) as f:
    f.start()