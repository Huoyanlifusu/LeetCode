# 创建型
# 1.简单工厂

class TechnicalBooks(object):
    def publish(self):
        return "Python-Book"

class LiteraryBooks(object):
    def publish(self):
        return "Remeo and Juliet"

it_books = TechnicalBooks()
lt_books = LiteraryBooks()

class SimpleFactory(object):
    @staticmethod
    def publish_book(name):
        if name == "technical":
            return TechnicalBooks()
        elif name == "literary":
            return LiteraryBooks()
    
it_book2 = SimpleFactory.publish_book("technical")
lit_book2 = SimpleFactory.publish_book("literary")
s1 = it_book2.publish()
s2 = lit_book2.publish()

print(s1, s2)

# 简单工厂的好处在于 把实例化的过程统一到一个工厂里面
# 给用户提供接口，从而把真正的类，以及其中的逻辑隐藏起来
# 缺点在于，如果有新的类进来，就要修改源码，违背了开闭原则

# 2.抽象工厂
import abc

class Solider(object):
    def __init__(self, gun):
        self.gun = gun
    
    def fire(self):
        self.gun.pong()

class GunFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gun(self):
        pass

class Gun(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def pong(self):
        pass

class Rifle(Gun):
    def pong(self):
        print("Rifle Fire! Pong!")

class HangGun(Gun):
    def pong(self):
        print("HangGun Fire! Pong!")