'''str1=input()
li=[]
for s in str1:
    if s not in li:
     for i in range(0,2):
        li.append(s)
print(li)

from _ast import Global

for j in range(1,10,-1):
    print(Global(j))
a=int(input())
b=int(input())
for i in range(a,b,3):
    print(i)

sumeven=0
sumodd=0
for i in range(1,11):
    #j=i%2;
    if i%2==0:
        sumeven=sumeven+i
    else:
        sumodd=sumodd+i
print("sum of even number is ",sumeven)
print("sum of odd number is ",sumodd)

for i in range(10,1,-1):
    print(i)X
str1="WELCOME"
for i in str1:
    print(i)

str1="WELCOME"
print(str1[2])
str1[2]="l"

str1="WELCOME"
print(str1[::-1])

str1="WELCOME"
count=0
for i in str1:
     count=count+1
print(count)

str1="WELCOME"
count=0
for i in str1:
    if i=='E':
     count=count+1
print(count)

str1="WELCOME"
count=0
for i in str1:
    if i is 'E':
     count=count+1
print(count)


str1="WELCOME"
for i in str1:
    count = 0
    if i is 'E':
     count=count+1
print(count)

str1="WELCOME"
l1=[]
l2=[]
cnt=0
for i in str1:
    cnt=cnt+1
    if cnt>3:
        l2.append(i)
    else:
        l1.append(i)
print(''.join(l1))
print(''.join(l2))

li=[]
li2=[]
for i in range(1,10):
    if i%2==0:
        li.append(i)
    else:
        li2.append(i)
print("The even number list :",li)
print("The odd number list :",li2)


l1=['1','A','2','B']
c1=0
c2=0
for i in l1:
    if i in '[A-Z]':
        c1=c1+1
    else:
        c2=c2+1
print(c1)
print(c2)

l1=['1','A','2','B']
c1=0
c2=0
for i in l1:
    if ord(i)>=65 and ord(i)<=90:
        c1=c1+1
    else:
        c2=c2+1
print(c1)
print(c2)

l1=[1,'A',2,'B']
c1=0
c2=0
for i in l1:
    if type(i)==str:
        c1=c1+1
    else:
        c2=c2+1
print(c1)
print(c2)

l1=['1','A','2','B']
c1=0
c2=0
for i in l1:
    if i.isnumeric():
        c1=c1+1
    else:
        c2=c2+1
print(c1)
print(c2)'''

import re
"""l1=['1','A','2','B']
li1="1A2B"
c1=0
c2=0
match=re.findall(r'[A-Z]',l1)
print(match)
for i in l1:
    if i in match:
        c1=c1+1
    else:
        c2=c2+1
print(c1)
print(c2)"""



