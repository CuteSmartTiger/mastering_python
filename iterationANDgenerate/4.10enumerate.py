# 4.10 序列上索引值迭代
# enumerate() 函数
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 2):
    print(idx, val)
# 2 a
# 3 b
# 4 c

def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 5):
            print(lineno,line)
            fields = line.split()
            try:
                count = int(fields[1])
                print(fields)
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

parse_data("test.txt")

from collections import defaultdict
word_summary = defaultdict(list)

with open('test.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        # 字典赋值
        word_summary[word].append(idx)
print(word_summary)
