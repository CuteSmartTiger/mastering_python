记录： 一个脚本在连续运行后，使用内存越来越大，在循环后手动添加gc.collect()没有作用。


尝试方法：

去除所有函数中当作参数传入的全局变量

使用全局redis对象，不再当作参数传入

循环末尾使用del显式删除变量循环中生成的变量，然后调用gc.collect()

主函数结尾删除函数中使用的变量，怀疑这写部分有可能循环引用。


update: 还是有内存泄漏，尝试将所有的语句尽可能封装在函数中，函数执行完成后，变量会回收。

--没解决问题 删除了一个igetui的全局的class，每次调用时再创建，使用完删除，观察。

update again: 使用objgraph在主函数开始和结束的时候objgraph.show_growth() 发现tuple在每次运行结束之后都会增加，逐个检查主函数中的子函数，发现tuple增加很可能是由于数据库操作函数引起，查看函数运行时输出，发现数据库操作的时候有警告，"Warning: Truncated incorrect time value: "，怀疑可能时在这个时候抛出警告引起了内存泄漏，查看警告个数和增加的tuple个数相差无几，于是修改sql，之后再次用objgraph.show_growth()查看，函数运行两次后，不再有tuple增加，观察一段时间，memory使用稳定。



https://www.cnblogs.com/buxizhizhoum/p/7486188.html
