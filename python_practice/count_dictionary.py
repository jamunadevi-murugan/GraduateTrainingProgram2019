str1=input("Enter the string : ")
list1=list(str1)
keys=[]
values=[]
list2=[]
dict1={}
str2=''
for i in range(0,len(list1)):
    c=list1.count(list1[i])
    keys.append(c)
    values.append(list1[i])
for j in range(0,len(list1)):
    dict1[values[j]]=keys[j]
    list2.append(str(values[j]))
    list2.append(str(keys[j]))
'''for k in dict1:
    list2.append(str(k))
    list2.append(str(dict1[k]))'''
str2=''.join(list2)
print(str2)
print(dict1)

'''str2=input("Enter the string : ")
dict2={}
for i in str2:
    if i in dict2:
        v=dict2.get(i)
        dict2[i]=v+1
    else:
        dict2[i]=1
print(dict2)'''
