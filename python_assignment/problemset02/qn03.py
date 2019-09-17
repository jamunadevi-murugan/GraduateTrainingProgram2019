def factI(n):
    fact=1
    num=n
    if n==0 or n==1 or n<0:
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
    return fact

def factR(n):
    if n==0 or n==1 or n<0:
        return 1
    else:
        return n*factI(n-1)

number=int(input("Enter an integer to find the factorial of a number:"))
factorial=factI(number)
factorial1=factR(number)
print("(Iterative Method)Factorial of ",number," is ",factorial)
print("(Recursive Method)Factorial of ",number," is ",factorial1)