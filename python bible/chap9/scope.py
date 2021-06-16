#part 1
#global and local variables
a = 250

def f1():
    b = 250 +10
    print(b)

def f2():
    a = 50 
    print(a)

f1()
f2()
print(a)

#part 2
a = [1,2,3]

def f1():
    a[0] = 5

    print(a)

def f2():
    print(a)

f1()
f2()
print(a)


a = 250

def f1():
    global a
    a = 100 #global
    print(a)

def f2():
    a = 50 #local
    print(a)

f1()
f2()
print(a)
