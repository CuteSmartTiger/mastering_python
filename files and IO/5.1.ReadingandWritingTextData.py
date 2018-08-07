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
with open('test.txt', 'wt',encoding="utf-8") as f:
    f.write(text1)
    f.write(text2)
    f.close()
    # for line in f:
    #     print(line)

with open('test.txt', 'rt') as f:
    f.read()


# Redirected print statement
with open('test.txt', 'wt',newline="",encoding="utf-8",errors="ignore") as f:
    print(file=f)
    print(file=f)