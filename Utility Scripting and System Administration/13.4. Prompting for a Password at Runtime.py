# 13.4. Prompting for a Password at Runtime

import getpass
# getpass 模块输入用户名是没有提示的
user = getpass.getuser()
# getpass 模块输入密码是隐式输入
passwd = getpass.getpass()
def svc_login(user,passwd):
    passwd = str(passwd)
    if 'Y' in user and passwd =="1111":
        return True
    else:
        return False

if svc_login('Y', 1111):
    print('Yay!')
else:
    print('Boo!')


# input有提示
user = input('Enter your username: ')
