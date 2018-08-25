# 9.24. Parsing and Analyzing Python Source

# 1前言：

# import ast
# ex = ast.parse('2 + 3*4 + x', mode='eval')
# print(ex)
# print(ast.dump(ex))
# Expression(body=BinOp(left=BinOp(left=Num(n=2), op=Add(),
#             right=BinOp(left=Num(n=3), op=Mult(), right=Num(n=4))),
#             op=Add(), right=Name(id='x', ctx=Load())))

# 分析这些节点最简单的方法就是定义一个访问者类，
# 实现很多 visit_NodeName() 方法， NodeName() 匹
# 配那些你感兴趣的节点

# 2.定义一个类，记录了哪些名字被加载、存储和删除的信息
import ast
# 定义类
class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)

# Sample usage
if __name__ == '__main__':
    # Some Python code
    code = '''for i in range(10):print(i)'''
    # Parse into an AST
    top = ast.parse(code, mode='exec')
    # Feed the AST to analyze name usage
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)