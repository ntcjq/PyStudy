import keyword

#关键词
print(keyword.kwlist)
"""
多行注释

Python 中有六个标准的数据类型：
Number  数字
String  字符串
List    列表    [1,2,3]
Tuple   元组    (1,2,3)             #元素不能修改
Set     集合    {'Alice','3258'}    #无序、不重复
Dictionary  字典{'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
Python3 的六个标准数据类型中：

不可变数据:Number、String、Tuple
可变数据:List、Dictionary、Set
"""
'''
多行注释
'''

#乘法口诀表
for x in range(1, 10):
    for y in range(1, 10):
        # print(x, "*", y, "=", x * y, end="\t")
        # print('{0} * {1} = {2}'.format(x, y, x * y), end="\t")
        #Python 3.6以后写法
        # print(f'{x} * {y} = {x * y}', end="\t")
        #%d=数字  %s=字符串 \t=table键
        print("%d*%d=%d" % (y, x, x * y), end="\t")
    print()  #换行

#键盘输入
say = print("请输入你想说的话：")
print(say)