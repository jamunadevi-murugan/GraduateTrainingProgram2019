def sumDigits(s):
    digitsum=0
    try:
        for i in s:
            digitsum+=int(i)
        return digitsum
    except ValueError:
        return len(s)

str1=input("Enter a string to find the sum : ")
print(sumDigits(str1))