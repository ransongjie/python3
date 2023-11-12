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
#不定长参数：*varTuple **varDict


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


# 生成式
def f6():
    g=[x**2 for x in range(3)]
    print(g) #[0, 1, 4]

# 生成器
def f7():
    g=(x**2 for x in range(3))
    for v in g:
        print(v) #0 1 4

# 自定义生成器
def f8():
    fg=fibonacci_generator(5)
    for v in fg:
        print(v)

def fibonacci_generator(n):
    a,b,count=0,1,0
    while True:
        if count>n:
            return
        # yield 返回一个值并暂停执行，在下一次调用生成器函数时从上次暂停的地方继续执行
        yield a
        a,b=b,a+b
        count+=1
        
#自定义生成器2
#通过使用 yield，我们可以实现惰性计算、按需生成值的功能，从而节省内存和提高效率。
#生成器函数在迭代和处理大量数据时非常有用，尤其是当数据无法一次性放入内存时。
def f9():
    gen = my_generator()
    print(next(gen))      #输出: 1
    print(gen.send('Hello'))  #send给value，输出: 2
    print(next(gen))      #输出: 3

def my_generator():
    value = yield 1 #生成器返回1，需要value
    print('Received:', value) #输出: Received: Hello
    yield 2
    yield 3

#自定义迭代器
def f10():
    myIter=MyIterator(1,3)
    it=iter(myIter)
    print(next(it)) # 1
    print(next(it)) # 2
    
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            return value

if __name__ == "__main__":
    # f1()
    # f2()
    # f3()
    # f4()
    # f5()
    # f7()
    # f8()
    # f9()
    f10()