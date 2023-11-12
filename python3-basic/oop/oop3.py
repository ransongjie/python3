# encoding: utf-8

# 多继承

class People:
    #基本属性
    name = ''
    age = 0
    #定义私有属性, 私有属性在类外部无法直接进行访问
    __weight = 0
    #构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承
class Student(People):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        People.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
class Speaker():
    topic = ''
    name = 'spkear'
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个Programer，我擅长的编程语言是 %s"%(self.name,self.topic))
    def get_name(self):
        print(self.name)
        
#多继承
class Sample(Speaker,Student):
    sample =''
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)
    def get_sample(self):
        print("my sample")
        return "my sample"
    def get_name(self):
        """
        重写父类Speaker的方法
        """
        print("sample name")
 
sample = Sample("xcrj",25,80,4,"Python 3")
sample.speak()   #父类有相同成员方法，默认调用括号中参数考前父类的方法
sample.get_sample() #独有方法
sample.get_name() #sample name