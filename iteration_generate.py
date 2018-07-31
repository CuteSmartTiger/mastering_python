# 需要掌握的知识点：__iter__的用法

# 疑惑点：思考如何自定义next方法，哪些对象可以使用next方法，next方法的实例用法深度解析

# 优化点：

# 4.2 委托迭代
# 定义一个类，然后在类中定义方法
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

print(root._children)
# [Node(1), Node(2)]