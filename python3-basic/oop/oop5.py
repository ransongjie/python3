# encoding: utf-8


class Parent:

    def add(self, x):
        y = x + 1
        print(y)

    def div(self, x):
        print("Parent div")


class Son(Parent):

    def add(self, x):
        super().add(x)

    def div(self, x):
        print("Son div")


s = Son()
s.add(2)  # 3
super(Son, s).div(0)  # Parent div
