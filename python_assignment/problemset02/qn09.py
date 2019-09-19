'''import math
def NewtonSqrt(a):
    x=a
    lastvalue=0
    for i in range(1,500):
        lastvalue = x
        x=(x+a/x)/2
        if(x==lastvalue):
            break
    return x

s=int(input("Enter an integer to find the square root : "))
ns=NewtonSqrt(s)
print("Newton Square Root of ",s," is ",ns)
s1=math.sqrt(s)
print(s1)
print(abs(ns-s1))'''
import math
def NewtonSqrt(a):
    x=a
    lastvalue=0
    for i in range(1,500):
        lastvalue = x
        x=(x+a/x)/2
        if(x==lastvalue):
            break
    return x

Number=[]
NewtonSqrtnumber=[]
math_sqrt=[]
difference=[]
for i in range(1,10):
    Number.append(i)
    NewtonSqrtnumber.append(NewtonSqrt(i))
    math_sqrt.append(math.sqrt(i))
#print(Number)
#print(NewtonSqrtnumber)
#print(math_sqrt)
for j in range(0,len(NewtonSqrtnumber)):
    diff=abs(NewtonSqrtnumber[j]-math_sqrt[j])
    difference.append(diff)
#print(difference)
print("{:^10}|{:^20}|{:^20}|{:^25}".format("Number","NewtonSqrt","math.sqrt","Difference"))
print("--------------------------------------------------------------------------------"
      "")
for k in range(0,len(Number)):
    print("{:>10}|{:>20}|{:>20}|{:>25}".format(Number[k],NewtonSqrtnumber[k],math_sqrt[k],difference[k]))