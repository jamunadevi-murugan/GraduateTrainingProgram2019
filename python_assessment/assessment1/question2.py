import math
list1=["five plus three","seven minus two","two plus eight minus five","eight divide four"]
list3=list1.copy()
list2=[]
str1=""
dict1={'one':'1',
       'two':'2',
       'three':'3',
       'four':'4',
       'five':'5',
       'six':'6',
       'seven':'7',
       'eight':'8',
       'nine':'9',
       'ten':'10',
       'plus':'+',
       'minus':'-',
       'divide':'/',
       'multiply':'*'
       }
for i in range(0,len(list1)):
    str1=list1[i]
    for j in dict1:
        if j in str1:
            str1=str1.replace(j,dict1[j])
    list1[i]=str1
for j in range(0,len(list1)):
    value=eval(list1[j])
    list1[j]=math.floor(value)
for k in list1:
    for l in dict1:
        if str(k)==dict1[l]:
            list2.append(l)
print(list3)
print(list2)