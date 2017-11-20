#!/usr/bin/env python3
# coding=gbk

#����һ������ĸ����ʵ����һ������Ķ���


#object �����ж�������ȣ� init ��ǰ���������»���
#self ָ����ǰ����
class Dog(object):
    '''
    __init__�������ڶ��󴴽���ִ�еģ�������������������ıر����������������ʵ�ʺ�����__new__(),��__new__()�Ǽ̳�����object�����߱��ĺ������˴����Բ�������ʵ�֣�������__new__()����ֵ����ָ���Ƿ�ִ��__init__()
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
�̳�
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
Java C++ �У�������private��protected�ؼ�ֵ�������Ժͷ��������ǿ������Ժͷ����ܷ��ⲿ����������ʣ���Python��Լ�������Է�����ǰ���__�������»��ߣ����ܾ��ⲿ�ķ���
'''
class Shiyanlou:
    __private_name = 'shiyanlou'

    def __get_private_name(self):
        return self.__private_name

class Animal_1(object):
    owner = 'jack' #��̬���� ֱ�Ӵ�����ʣ�����Ҫʵ����������ܷ��ʣ���Ҫ������__init__֮ǰ,��̬�����෽�����Է�����ľ�̬����
    def __init__(self, name):
        self._name = name
    def showself(self):
        pass
        #����ĵ�һ������ʵ������,�����ӡ���޷���ӡ��,cls�޶���,��̬����ֻ�����෽����ʹ��
        #print("owner", cls.owner,"self ", self)
    #�෽�� �п��Է�����ľ�̬������ע���෽���еĵ�һ�������Ĵ���������󣬶�����ʵ������
    @classmethod
    def get_owner(cls):
        print("hello ",cls)
        return cls.owner
    #staticmethod ��classmethod�е����ƣ�����ʱ����Ҫʵ���Ĳ��룬���������෽����������һ��cls����,��̬������Ӧ�ó����ǵ�һ��������ȫ���Էŵ������浥��ʵ�ֵ�ʱ���������������໹�е���ϵ����ô���������ܸ��õ���֯�����߼�����ô���Կ���ʹ�����еľ�̬����
    @staticmethod
    def order_animal_food():
        print('ording...')
        print('ok')

class Animal_2(object):
    def __init__(self, name):
        self._name = name
    #���������һ��������ʹ�ã�����property����ʵ��Python�ָ��getter/setter,������ͨ��property��ú��޸Ķ����ĳһ������
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
    dog = Dog('zuan')   #����һ������
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


#python��̬���͵�������û����ô���Ե����ֶ�̬����������Ϊ��python����������������ָ���������͵�ֵ
    animals = [Dog1("abc"), Cat1('abc1'), Dog1('abc2'), Cat1('abc3')]

    for animal in animals:
        animal.make_sound()


    s = Shiyanlou()
    #s.__private_name #ֱ�ӷ�����������
    #�����淽��ȥ����Լ����˽�еķ���������
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
