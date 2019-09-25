'''#map
multiply=lambda a:a*2
print(multiply(5))

input=[1,2,3,4,5]
print(map(lambda a:a*2,input))

input=[1,2,3,4,5]
print(list(map(lambda a:a*2,input)))

#filter
input=[-1,-2,-3,0,1,2,3,4,5]
print(list(map(lambda a:a>0,input)))

input=[-1,-2,-3,0,1,2,3,4,5]
print(list(filter(lambda a:a!=0,input)))

vowels='aeiou'
input1=['a','b','c','d','e','f','g']
input2=input()
print(list(filter(lambda a:a not in vowels,input2)))
print(list(filter(lambda a:a not in vowels,input1)))

string="ACCENTURE"
list1=list(map(lambda a:a+'1',string))
print(''.join(list1))

from functools import reduce
list1=[1,2,3,4]
print(reduce(lambda a1,a2:a1*a2,list1))

emp='11729547'
list1=''.join(map(lambda a:a*2,emp))
print(list1)

list2=[2,5,8]
if list2[0]>=list2[1] and list2[0]<=list2[2]:
    print("True")
else:
    print("False")

l1=[1,1,3,2,1,2,4,5,3]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

l1=[1,1,3,2,1,2,4,5,3]
l2=[]
for i in l1:
    if i in l2:
        continue
    else:
        l2.append(i)
print(l2)

list1=[1,3,2,1,4,5,2,3]
list2=[]
[list2.append(i) for i in list1 if i not in list2]
print(list2)

s1="This is a new batch in this year"
li1=s1.split(' ')
for i in li1:
    if len(i)%2==0:
        print(i)

s1="This is a new batch in this year"
li1=s1.split(' ')
li2=[]
for i in li1:
    li2.append(i[0])
print(li2)

li2=[i[0] for i in li1]
print(li2)

import math
number=input("Enter : ")
if number.isnumeric():
    print(math.sqrt(int(number)))
else:
    print("Not a Valid Input")'''

# import math
# number=input("Enter : ")
# try:
#     print(math.sqrt(int(number)))
# except ValueError:
#     print("Not a valid exception")
#
# list1=[1,3,2,1,4,5,2,3]
# list2=[]
# [list2.append(i) for i in list1 if i not in list2]
# print(list2)

prime=[i for i in range(1,50) if i!=1 and 0 not in [i%j for j in range(2,i)]]
print(prime)

prime1=[i for i in range(1,50) if i!=1 and all(i%j!=0  for j in range(2,i))]
print(prime1)

primedict={i:('Yes' if i!=1 and 0 not in [i%j for j in range(2,i)] else 'No') for i in range(1,10)}
print(primedict)

prime=[i for i in range(1,50) for j in range(2,i) if i%j==0 and i!=j]
list2=[i for i in range(1,50) if i not in prime]
print(list2)