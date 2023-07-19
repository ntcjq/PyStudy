
#string 字符串
str="W3cschool"
print(type(str))
str[2:3]    #使用截取方式，用正序进行截取
str[2:-6]   #使用截取方式，正序和倒序混合使用
str[-7:-6]  #使用截取方式，使用倒序进行截取
str[-7] #使用负索引获取单个字符C
str[2]  #使用正索引获取单个字符C


#tuple  元祖 元组中的元素值是不允许修改的
t = (1,2,3)
print(type(t))
t[0]    #获取第一个元素
tup = (50,) #元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当做运算符使用

#list   列表
l = ['Google', 'W3Cschool', 1997, 2000]
print(type(l))
l[0]    #list的第一项
l[-1]   #list的最后一项
list[0:3]   #list的前3项
del list[0] #按照索引删除元素
list.remove(1997)  #删除指定元素
list[1] = 2023 #修改元素

#set    集合 集合是一个无序的不重复元素序列
se = {'a','b','c','se'}
print(type(se))
se.add('x')
se.remove('a')


#dict   字典
d = {'key1':'value1','key2':'value2'}
print(type(d))
d["key1"] #获取值
d['key2'] = 8;  # 更新
d['School'] = "教程"    # 添加
del d['School'] #删除