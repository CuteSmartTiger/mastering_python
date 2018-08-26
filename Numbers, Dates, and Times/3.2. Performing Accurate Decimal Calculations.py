# 3.2. Performing Accurate Decimal Calculations

from decimal import Decimal
# >>> a = Decimal('4.2')
# >>> b = Decimal('2.1')
# >>> a + b
# Decimal('6.3')
# >>> print(a + b)
# 6.3
# >>> (a + b) == Decimal('6.3')
# True

# decimal 模块的一个主要特征是允许你控制计算的
# 每一方面，包括数字位数和四舍五入运算

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
# 0.7647058823529411764705882353
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)


# nums = [1.23e+18, 1, -1.23e+18]
# sum(nums) # Notice how 1 disappears
import math
# math.fsum(nums)
