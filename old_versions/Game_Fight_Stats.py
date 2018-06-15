import random

def func():
    if True == True:
        a = random.randint(1,3)
        print(a)
        b = random.randint(1,3)
        print(b)
        c = random.randint(1,3)
        print(c)
    list = [a,b,c]
    return [a,b,c,True]
list2 = func()
print(list2)
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])