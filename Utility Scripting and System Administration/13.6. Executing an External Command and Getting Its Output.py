# 13.6. Executing an External Command and Getting Its Output
import subprocess

# out_bytes = subprocess.check_output(['ls','-a'])
#
# out_text = out_bytes.decode('utf-8')
# print(out_text)
#
# try:
#     out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
# except subprocess.CalledProcessError as e:
#     out_bytes = e.output # Output generated before error
#     code = e.returncode # Return code
#
# # ，check_output() 仅仅返回输入到标准输出的值。
# # 如果你需要同时收集标准输出和错误输出，使用 stderr 参数
# out_bytes = subprocess.check_output(['cmd','arg1','arg2'],stderr=subprocess.STDOUT)
#
# try:
#     out_bytes = subprocess.check_output(['cmd','arg1','arg2'], timeout=5)
# except subprocess.TimeoutExpired as e:
#     e.timeout
#
# # 运行在Linux上执行的命令，以数组的方式进行组合，将shell设置为true
# out_bytes = subprocess.check_output('grep python | wc > out', shell=True)
#


# 如果需要对子进程做更复杂的交互，比如给它发送输入，
# 可直接使用 subprocess.Popen
import subprocess
# Some text to send
text = b'''hello worldthis is a testgoodbye'''
# Launch a command with pipes
p = subprocess.Popen(['wc'],stdout = subprocess.PIPE,stdin = subprocess.PIPE)
# Send the data and get the output
stdout, stderr = p.communicate(text)
# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
print(out)
print(err)