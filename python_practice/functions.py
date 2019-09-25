'''def printHello():
    print("Hello")
printHello()

def printInteger(a):
    print(a)
    return 2
a=printInteger(1)
print(a)

def sum(a,b):
    c=a+b
    if c>0:
        return "Success"
    else:
        return "fail"
print(sum(1,2))

def sum(a,b):
    c=a+b
    return c
def total():
    tot=0
    c=sum(5,5)
    if c==10:
        tot=c+1
    return tot
print(total())'''

def sum(a,b=0):
    c=a+b
    return a,b,c
temp1,temp2,temp3=sum(1,)
print(temp1)
print(temp2)
print(temp3)