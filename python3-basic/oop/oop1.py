# encoding: utf-8


def f1():
    myClass = MyClass()
    print(myClass.i)  #12345
    print(myClass.f())  #hello world


class MyClass:
    i = 12345

    def f(self):
        return "hello world"


def f2():
    x = Complex(3.0, -4.5)
    print(x.r, x.i)  # (3.0, -4.5)
    print(x.__class__)  #__main__.Complex
    # print(x.__weight) #私有属性 只能在类中调用
    # print(x.__get_weight()) #私有方法 只能在类中调用
    pass


class Complex:
    __weight = 0  # 私有属性

    def __init__(self, realpart, imagpart):
        """
        构造方法
        """
        self.r = realpart
        self.i = imagpart

    def __get_weight(self):
        """
        私有方法
        """
        return self.__weight

if __name__ == "__main__":
    # f1()
    # f2()
    pass
