"""
python面向对象编程
什么是面向对象：
类、方法、类变量的定义
实例引用、实例变量使用


面向对象开发就是不断的创建对象、使用对象、操作对象做事情
不同的人负责不同的模块并最后组装在一起
面向对象解释：
语言层面：封装代码和数据
规格层面：对象是一系列可被使用的公共接口
从概念层面：对象是某种拥有责任的抽象


程序设计规则：
1、有哪些类
2、每个类多有哪些属性和行为
3、类与类之间存在的关系


类：抽象的概念 一类事物
方法：类中定义的函数，对外提供的服务
类变量：类变量在整个实例化的对象中是公用的
实例引用：实例化一个对象 对象？
实例变量：以self.变量名的方式定义的变量

"""

#创建一个人类
#通过关键字class定义了一个类
class Person:
    #类变量
    name = "default"
    age = 0
    gender = "male"
    weight = 0
    #构造方法，在类实例化的时候被调用
    def __init__(self, name, age, gender, weight):
        #self。变量名的方式，访问到的是实例的变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    @classmethod  #增加装饰器使其变成类方法以使类可以直接访问调用
    def eat(self):
        print(self.name,"eating")

    def play(self):
        print(self.name,"playing")

    def jump(self):
        print("jumping")

    # def set_name(self, name):
    #     #self.name  调用类中的name属性
    #     self.name = name
    # def set_age(self, age):
    #     self.age = age

#实例化类

xm = Person("小明", 18, "男", 90)  #调用init方法
# zs.set_name("zhangsan")
# zs.set_age(20)
name_xm = xm.name
age_xm = xm.age
gender_xm = xm.gender
weight_xm = xm.weight
xm.eat()
xm.play()

print("zhangsan的名字是:",name_xm, "年龄是：" ,age_xm, "性别是 ",gender_xm, "体重是 ", weight_xm)

#类变量和和实例变量的区别，
#类变量和实例变量都是可以修改的
#类变量是需要类来访问的，实例变量需要实例来访问
#类方法需要添加一个修饰器 @classmethod
print(Person.name)
Person.name = "game"
print(Person.name)


print(xm.name)
xm.name = "李丽"
print(xm.name)


#类方法是实例方法
#类方法不能访问实例方法

Person.eat()