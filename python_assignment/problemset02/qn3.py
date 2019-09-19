def factR(n):
    if n==0 or n<0 or n==1:
        return 1
    else:
        return n*factR(n-1)
n1=int(input("Enter an integer to find factorial : "))
j=factR(n1)
print("The factorial of ",n1," is ",j)