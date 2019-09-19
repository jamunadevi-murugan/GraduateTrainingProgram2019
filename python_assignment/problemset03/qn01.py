def is_palindrome(s):
    if s[::-1]==s:
        return True
    else:
        return False
str1=input("Enter a string whether the given string is palindrome or not : ")
if(is_palindrome(str1)==True):
    print("Palindrome")
else:
    print("Not a Palindrome")