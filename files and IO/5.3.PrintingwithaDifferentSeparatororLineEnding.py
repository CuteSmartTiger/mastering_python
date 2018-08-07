# 5.3 使用其他分隔符或行终止符打印

# 以使用在 print() 函数中使用 sep 和 end 关键字参数
print('ACME', 50, 91.5, sep=',', end='!!\n')

for i in range(5):
    print(i, end=' ')

print(','.join(('ACME','50','91.5')))
# str.join() 的问题在于它仅仅适用于字符串

row = ('ACME', 50, 91.5)
print(','.join(str(x) for x in row))

#  * 的用法
print(*row,end=",")
# ACME 50 91.5,

print(*row,sep=",")
# ACME,50,91.5