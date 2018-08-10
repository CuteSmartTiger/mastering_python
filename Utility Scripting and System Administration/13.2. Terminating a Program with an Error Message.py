# 13.2. Terminating a Program with an Error Message

raise SystemExit('It failed!')
# It failed!



# 等同于：
import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)