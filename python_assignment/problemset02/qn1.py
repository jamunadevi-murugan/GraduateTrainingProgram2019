a1=int(input("Enter first Integer : "))
b1=int(input("Enter second Integer : "))
a=0
b=0
remainder=0
if a1>b1:
    a=a1
    b=b1
else:
    a=b1
    b=a1
if b==0:
    print("The GCD of ",a1," and ",b1," is : ",a)
else:
 while(b!=0):
    remainder=a%b
    a=b
    b=remainder
    if remainder==0:
        print("The GCD of ",a1," and ",b1," is : ",a)