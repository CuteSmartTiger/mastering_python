# 3.1. Rounding Numerical Values

# 纲要：四舍五入与格式化保留精确度的区别

# >>> round(1.23, 1)
# 1.2
# >>> round(1.27, 1)
# 1.3
# >>> round(-1.27, 1)
# -1.3
# >>> round(1.25361,3)
# 1.254

# >>> a = 1627731
# >>> round(a, -1)
# 1627730
# >>> round(a, -2)
# 1627700
# >>> round(a, -3)
# 1628000

x = 1.23456
print(format(x, '0.2f'))
# '1.23'
print(format(x, '0.3f'))
# '1.235'
print('value is {:0.3f}'.format(x))
# 'value is 1.235'

# 不能允许这样的小误差(比如涉及到金融领域)，那么就得考虑使用 decimal 模块