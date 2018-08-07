# 使用模式为 rb 或 wb 的 open() 函
# 数来读取或写入二进制数据。

# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()

# Write binary data to a file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')
# 在读取二进制数据时，需要指明的是所
# 有返回的数据都是字节字符串格式的，
# 而不是文本字符串。 类似的，在写入的
# 时候，必须保证参数是以字节形式对外暴
# 露数据的对象(比如字节字符串，字节数
# 组对象等)。


# 注意：索引和迭代动作返回的是字节的值而不是字节字符串
b = b'Hello World'
print(b[0])  #72

for c in b:
    print(c,end=",")
# 72,101,108,108,111,32,87,111,114,108,100,


# 如果你想从二进制模式的文件中
# 读取或写入
# 文本数据，
# 必须确保要进行解码和编码操作

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))



# 二进制I/O还有一个鲜为人知的特
# 就是数组和C结构体类型能直接被写入
# ，而不需要中间转换为自己对象
import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin','wb') as f:
    f.write(nums)