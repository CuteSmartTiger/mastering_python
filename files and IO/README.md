#### 内容框架结构：
```
介绍相关知识点的目的及用途
疑惑的知识点，备注时间
本章节的重点知识点在其当前的文件内注明
注意事项
```

- 疑惑的知识点
***201808***
```
描述符，5.6节有提到

哪些文件以文本模式打开，哪些需要以二进制模式

```
- 注意事项：
 - 1.python的可变对象（list，dict）与不可变对象（int,string,float,tuple），注意
        这两个在函数参数传递上的区别，好好体会
    ```
def test(a_int, b_list):
    a_int = a_int + 1
    b_list.append('13')
    print('inner a_int:' + str(a_int))
    print('inner b_list:' + str(b_list))

if __name__ == '__main__':
    a_int = 5
    b_list = [10, 11]

    test(a_int, b_list)

    print('outer a_int:' + str(a_int))
    print('outer b_list:' + str(b_list))

输出：
inner a_int:6
inner b_list:[10, 11, '13']
outer a_int:5
outer b_list:[10, 11, '13']


    ```
