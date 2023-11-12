# encoding: utf-8

# try except
def f1():
    while True:
        try:
            x = int(input("请输入一个数字: "))
            print(x)
            break;
        except ValueError:
            # 发生ValueError执行的代码
            print("您输入的不是数字，请再次尝试输入！")

# else
def f2():
    while True:
        try:
            x = int(input("请输入一个数字: "))
            print(x)
        except ValueError as err: # as 异常对象
            # 发生ValueError执行的代码
            print("您输入的不是数字，请再次尝试输入！",err)
        else:
            # 没有发生异常将执行的代码
            print("没有发生异常")
            break

# finally
def f3():
    while True:
        try:
            x = int(input("请输入一个数字: "))
            print(x)
        except ValueError:
            # 发生ValueError执行的代码
            print("您输入的不是数字，请再次尝试输入！")
        finally:
            print('无论异常是否发生都会执行。')

#raise Exception("异常信息")    
def f4():
    x = 10
    if x > 5:
         raise Exception('x 不能大于 5。x 的值为: ',x)          

#raise MyException("异常信息") 自定义异常
def f5():
    x = 10
    if x > 5:
         raise MyError('x 不能大于 5。x 的值为: ',x)

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#with 自动 close
#原理：上下文管理器，一个实现 __enter__ 和 __exit__ 方法的类。
#文件对象也实现了上下文管理器
#首先调用 __enter__ 方法，然后执行 with 语句中的代码，最后调用 __exit__ 方法。 
#即使出现错误，也会调用 __exit__ 方法，也就是会关闭文件流
def f6():
    with open("1.txt") as f:
        for line in f:
            print(line, end="")      

#assert expression 条件不满足就抛出 AssertionError
#等价于 if not expression: raise AssertionError
def f7():
    a=10
    assert a>10
   
if __name__ == "__main__":
    f7()