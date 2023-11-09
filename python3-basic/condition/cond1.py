#if
def f1():
    age=1
    if age <= 0:
        print("age <= 0")
    elif age == 1:
        print("age == 1")
    else:
        print("else")


#match case Python 3.10
# def f2():
#     code=1
#     match code:
#         case 1:
#             return "Bad request"
#         case 2:
#             return "Not found"
#         case 3:
#             return "I'm a teapot"
#         case _:  #_ default
#             return "default"

#while
def f3():
    sum = 0
    i = 0
    while i <= 10:
        sum +=i
        i+=1
    print(sum) #55

#while else
def f4():
    a = 4
    while a < 5:
        print (a, "小于 5")
        a = a + 1
    else:
        print (a, " 大于或等于 5")

#for
def f5():
    l = ["a", "b","c","d"]
    for a in l:
        print(a)
    
#for else    
def f6():
    x=1
    for x in range(6): #range(6) 0~5
        print(x)
        if x==2:
            continue #continue
        if x==5:
            break #break
    else:
        print("over")
    pass #pass

if __name__ == "__main__":
    # f1()
    # f2()
    # f3()
    # f4()
    # f5()
    # f6()
