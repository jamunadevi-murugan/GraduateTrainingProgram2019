def isIn(string1,string2):
    if string1 in string2 or string2 in string1:
        return True
    else:
        return False
str1=input("Enter first string : ")
str2=input("Enter second string : ")
if(isIn(str1,str2)):
    print("True")
else:
    print("False")
