# 检测结果标准输出
import unittest

def parse_int(s):
    return int(s)

class MyTest(unittest.TestCase):
        def test_what_you_want(self):
            self.assertRaises(ValueError, parse_int, 'N/A')

if __name__ == '__main__':
    unittest.main()

# 将测试结果重定向
import sys
def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)

if __name__ == '__main__':
    with open('testing.out', 'w') as f:
        main(f)

