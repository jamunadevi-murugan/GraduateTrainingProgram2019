def sumDigits(s):
    digitsum=0
    count=0
    try:
        for i in range(0,len(s)):
            if s[i].isdigit()!=True:
                count=count+1
            if count==len(s):
                return "No digits is found"
            else:
                raise Exception
    except Exception:
        for i in range(0, len(s)):
            if s[i].isdigit():
                digitsum += int(s[i])
        return digitsum

str1=input("Enter a string to find the sum : ")
print(sumDigits(str1))