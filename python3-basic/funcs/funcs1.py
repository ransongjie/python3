# encoding: utf-8


#函数定义
def f1():
    print(max(1, 2))


def max(a, b):
    """
    :param a
    :param b
    :return int
    """
    if a > b:
        return a
    else:
        return b


#参数传递 值传递
#不可变类型 函数内外不是引用同一个变量
#可变类型 函数内外是引用同一个变量
def f2():
    l = [1, 2]
    print(l)  #[1, 2]
    fa(l)
    print(l)  #[1, 2, 3]


def fa(l):
    l.append(3)


#必须参数：不传报错
#关键字参数：指定参数名传递 f(param=value)
#默认参数：定义时给参数默认值 f(age=10)
#不定长参数：*vartuple **vardict


#不定长参数
def f3():
    f3a(1, 2, 3)
    f3b(1, b=2, c=3)


#不定长参数: tuple
def f3a(arg1, *vtuple):
    print(arg1)  #1
    print(vtuple)  #(2,3)


#不定长参数: dict
def f3b(arg1, **vdict):
    print(arg1)  #1
    print(vdict)  #{'c': 3, 'b': 2}


#lambda表达式
def f4():
    #拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
    a = lambda a,b: a + b
    print(a(5,10)) #15

#强制位置参数 python3.8
def f5():    
    f5a(1, 2, 3, d=4, e=5, f=6)

#a 和 b 必须使用指定位置参数
#c 或 d 可以是位置形参或关键字形参
#e 和 f 要求为关键字形参   
def f5a(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f) #1 2 3 4 5 6

if __name__ == "__main__":
    # f1()
    # f2()
    # f3()
    # f4()
    # f5()