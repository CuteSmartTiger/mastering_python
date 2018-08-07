# test.txt
# line1: gogogo
# line2: comecome!

# # Read the entire file as a single string
# with open('test.txt', 'rt') as f:
#     data = f.read()
#
# # Iterate over the lines of the file
# with open('test.txt', 'rt') as f:
#     for line in f:
#         print(line)



# 没有f.close()使得上一次的文件始终处于打开状态。
# f.write()写的内容始终在内存中。所以，文件用完切记要关闭。

text1 = "test for fun"
text2 = "test for joy"
# Write chunks of text data
# 如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数。
with open('test.txt', 'wt',encoding="utf-8") as f:
    # 两次输入的内容在同一行
    f.write(text1)
    f.write(text2)
    f.close()
    # for line in f:
    #     print(line)



# Redirected print statement
# with open('test.txt', 'wt',newline="",encoding="utf-8",errors="ignore") as f:
# 使用打印重定向的方式可以写入数据成功
with open('test.txt', 'wt') as f:
    print(text1,file=f)
    print(text2,file=f)
    # 两次输入的内容分为两行