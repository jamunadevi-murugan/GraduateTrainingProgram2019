def is_anagram(str1,str2):
    count = 0
    s1 = sorted(str1)
    s2 = sorted(str2)
    if len(str1) == len(str2):
        if s1 == s2:
            return True
        else:
            return False
str1=input("Enter the 1st string : ")
str2=input("Enter the 2nd string : ")
if is_anagram(str1,str2)==True:
        print("Anagram")
else:
        print("Not Anagram")