import re
str1=input()
'''match=re.findall("[0-9]",str1)
if len(match)==8:
   match.pop(4)
   match.pop(4)'''
match=list(str1)
num=0
for i in match:
    if i=='/':
        match.remove(i)
for i in match:
    num=num+int(i)
str2=str(num)
li2=list(str2)
num1=0
for i in li2:
    num1=num1+int(i)
print("Numerology is :",num1)
