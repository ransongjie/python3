# encoding: utf-8

if __name__ == "__main__":
    #算数运算符 + - * / % ** //
    a = 2**3  #乘方 8
    print(a)  #8
    b = 2.9 // 2  #取整 往小了取
    print(b)  #1.0

    #比较运算符 == != > < >= <=

    #赋值运算符 = += -= *= /= %= **= //= :=
    a = [1, 2, 3, 4]
    if (n := len(a)) > 3:  #:= python 3.8 新增
        print(f"List is too long ({n} elements, expected <= 3)")

    #位运算符 & | ^ ~ << >>
    #-128~127
    #0x80->0x7f
    #计算机表示：1000,0000-+1->0111,1111
    c = ~-128  #按位取反，包括符号位
    print(c)  #127
    d = -128 << 1
    print(d)  #-256，不包括符号为
    e = -128 >> 1
    print(e)  #-64，不包括符号为

    #逻辑运算符 and or not

    #成员运算符 in, not int
    a = [1, 2, 3]
    if 1 in a:
        print("1 in a")

    #身份运算符 is, is not
    a = 10
    b = 10
    if a is b:  #等价于 id(a)==id(b)
        print("a和b标识符引用了同一个对象")
