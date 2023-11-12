# encoding: utf-8
# 运算符重载
# 运算符是类专有的方法 __类专有方法名__
class Operate:
   def __init__(self, a, b):
      self.a = a
      self.b = b
      
   def __add__(self,other):
      return Operate(self.a + other.a, self.b + other.b)
 
   def __str__(self):
      return 'Operate (%d, %d)' % (self.a, self.b)
   
v1 = Operate(2,10)
v2 = Operate(5,-2)
print (v1 + v2)