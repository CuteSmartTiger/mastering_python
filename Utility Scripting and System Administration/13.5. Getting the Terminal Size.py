# 13.5. Getting the Terminal Size



import os
sz = os.get_terminal_size()
# OSError: [WinError 6] 句柄无效。

print(sz)

os.terminal_size(columns=80, lines=24)

print(sz.columns)

print(sz.lines)