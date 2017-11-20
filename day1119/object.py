#!/usr/bin/env python3
# coding=gbk

#类是一个抽象的概念，而实例是一个具体的对象


#object 是所有对象的祖先， init 的前后有两个下划线
#self 指代当前对象
class Dog(object):
    '''
    __init__函数是在对象创建中执行的，并不是用来创建对象的必备函数，创建对象的实际函数是__new__(),而__new__()是继承来自object类所具备的函数，此处可以不必重新实现，并且在__new__()中升值可以指定是否执行__init__()
    '''
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name.lower().capitalize()
        #return self._name
    def set_name(self, value):
        self._name = value
    def bark(self):
        print(self.get_name() + 'is making sound wang wang wang...')

class Cat(object):
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name.lower().capitalize()
        #return self._name
    def set_name(self, value):
        self._name = value
    def bark(self):
        print(self.get_name() + 'is making sound miu miu miu...')

'''
继承
'''
class Animal(object):
    owner = "Anday"
    def __init__(self, name):
        self._name = name
    def get_name(self):
        print("self ", self)
        return self._name
    def set_name(self, value):
        self._name = value
    @classmethod
    def get_name2(cls):
        print("cls ", cls)
    def make_sound(self):
        pass

class Dog1(Animal):
    def make_sound(self):
        print(self.get_name() + " is making sound wang wang wang...")

class Cat1(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound miu miu miu...')

'''
Java C++ 中，可以用private和protected关键值修饰属性和方法，他们控制属性和方法能否被外部或者子类访问，在Python中约定在属性方法名前添加__（两个下划线）来拒绝外部的访问
'''
class Shiyanlou:
    __private_name = 'shiyanlou'

    def __get_private_name(self):
        return self.__private_name

class Animal_1(object):
    owner = 'jack' #静态变量 直接从类访问，不需要实例化对象就能访问，需要声明在__init__之前,静态变量类方法可以访问类的静态变量
    def __init__(self, name):
        self._name = name
    def showself(self):
        pass
        #传入的第一个参数实例对象,下面打印是无法打印的,cls无定义,静态变量只能在类方法中使用
        #print("owner", cls.owner,"self ", self)
    #类方法 中可以访问类的静态变量，注意类方法中的第一个参数的传入是类对象，而不是实例对象
    @classmethod
    def get_owner(cls):
        print("hello ",cls)
        return cls.owner
    #staticmethod 和classmethod有点类似，运行时不需要实例的参与，但并不像类方法那样传递一个cls参数,静态方法的应用场景是当一个函数完全可以放到类外面单独实现的时候，如何这个函数和类还有点联系，那么放入类中能更好的组织代码逻辑，那么可以考虑使用类中的静态方法
    @staticmethod
    def order_animal_food():
        print('ording...')
        print('ok')

class Animal_2(object):
    def __init__(self, name):
        self._name = name
    #将方法变成一个属性来使用，借助property可以实行Python分割的getter/setter,即可以通过property获得和修改对象的某一个属性
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    def make_sound(self):
        pass

class Cat2(Animal_2):
    def make_sound(self):
        print(self._name + " miu miu")

if __name__ == '__main__':
    dog = Dog('zuan')   #创建一个对象
    cat = Cat('Kitty')

    #print(dog._Dog__name)
    dog.bark()
    cat.bark()


    dog1 = Dog1('xiaoming')
    cat1 = Cat1('yuanyuan')
    print("dog1.__dict__ ", dog1.__dict__)
    print(Cat1.owner)
    dog1.make_sound()
    cat1.make_sound()


#python动态类型的语言中没有那么明显的提现多态的威力，因为在python中你可以用任意变量指向任意类型的值
    animals = [Dog1("abc"), Cat1('abc1'), Dog1('abc2'), Cat1('abc3')]

    for animal in animals:
        animal.make_sound()


    s = Shiyanlou()
    #s.__private_name #直接访问是有问题
    #用下面方法去访问约定的私有的方法和属性
    #obj._Classname__privateAttributeOrMethod
    print(s._Shiyanlou__get_private_name())
    print(s._Shiyanlou__private_name)

    print(Animal_1.owner)
    ani_1 = Animal_1("cat")
    print(ani_1.showself())

    print(Animal_1.get_owner())
    ani = Animal("Cat")
    print("22222", ani.get_name())
    print("11111", ani.get_name2())

    Animal_1.order_animal_food()

    cat_2 = Cat2('kitty')
    print(cat_2.name)
    cat_2.name = 'asdf'
    print(cat_2.name)
