def is_power(a,b):
    if a%b==0:
        for i in range(1,a):
            if b**i==a:
                return True
    else:
        return False
input("To find whether a is power of b")
a1=int(input("Enter a value : "))
b1=int(input("Enter b value : "))
print(is_power(a1,b1))