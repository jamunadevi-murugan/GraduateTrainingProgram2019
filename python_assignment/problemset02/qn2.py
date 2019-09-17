def is_power(a,b):
    if a%b==0:
        return True
    else:
        is_power(a/b,b)
    return False
input("A is a power of B")
a=int(input("Enter A : "))
b=int(input("Enter B : "))
print(is_power(a,b))