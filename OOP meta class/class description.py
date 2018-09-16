class Person:
    """类描述的文档，关于类的描述、作用、函数构造、属性等
    attributes: 用于描述类属性的含义，类型
    """
    age = 21

    def work(self,company,salary):
        """
        :param company:参数的含义，参数的类型，参数是否有默认值
        :param salary:
        :return: 返回值的含义，返回值的类型
        """
# 通过help函数查看文档信息
help(Person)


# 注释文档的生成：
# 方法一：pydoc,cmd中输入
# python3 -m pydoc module_name
# python3 -m pydoc -k name
# python3 -m pydoc -p port_id
# python3 -m pydoc -b
# python3 -m pydoc -w  module_name       #写入指定模块名称，生成对应的HTML文档

# 方法二：使用第三方模块
# Sphinx
# epydoc
# doxygen

