import re
def isPalindrome(s):
    s1 = s.lower()
    list1 = re.findall("\w+", s1)
    s1 = ''.join(list1)
    if len(s1)<1:
        return True
    else:
        if s1[0]==s1[-1]:
            return isPalindrome(s1[1:-1])
        else:
            return False

def testIsPalindrome(s):
    if (isPalindrome(s1) == True):
        print("Palindrome")
    else:
        print("Not a Palindrome")

s1=input("Enter a string to check whether the given string is palindrome or not : ")
testIsPalindrome(s1)