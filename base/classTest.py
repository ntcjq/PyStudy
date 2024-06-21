class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    # 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用下划线作为开头（方法同理）    '''
    # 在Python中，单下划线（_）和双下划线（__）都有表示属性和方法的不同级别的私有性，但它们的用途和作用有所不同。
    # 单下划线前缀是一个约定，表示属性或方法是“保护的”或“内部使用的”。这只是一个约定，主要用于提醒开发者这些成员不应该在类的外部直接访问，但并没有真正的访问限制。
    # 双下划线前缀会触发名称重整（name mangling），Python会将类中的双下划线前缀的属性或方法名重整为 _ClassName__attributeName 的形式，以实现更严格的封装。这使得这些成员在类外部更难访问，但并不是绝对不能访问。

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.__age < 18:
            print(f"{self.name}只能观看《熊出没》.")
        else:
            print(f"{self.name}s正在观看爱情大电影.")

    # 定义一个静态方法
    @staticmethod
    def breathe():
        print("Im breathe")


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student("Sea", 38)
    print(stu1.name)
    # 无法访问私有属性
    # print(stu1.__age)
    # 特殊方式访问私有属性
    # print(stu1._Student__age)

    # 给对象发study消息
    stu1.study("Python程序设计")
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student("王大锤", 15)
    stu2.study("思想品德")
    stu2.watch_movie()
    stu2.breathe()

    Student.breathe()


if __name__ == "__main__":
    main()
