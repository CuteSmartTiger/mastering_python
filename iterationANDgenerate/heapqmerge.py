
import heapq

# heapq.merge 可迭代特性意味着它不会立马读取所有序列
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c,end=',')
# 1,2,4,5,6,7,10,11

print('\n')
# heapq.merge() 需要所有输入序列必须是排过序的。 特别的，它并不会
# 预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检
# 测。 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一
# 直会持续直到所有输入序列中的元素都被遍历完,
# 这句话用一下示例可以解释
c = [1, 3, 7, 10]
d = [7, 5, 6, 11]
for c in heapq.merge(c, d):
    print(c,end=',')
# 1,3,7,7,5,6,10,11,


# 何合并两个排序文件
with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2', 'rt') as file2, \
    open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)