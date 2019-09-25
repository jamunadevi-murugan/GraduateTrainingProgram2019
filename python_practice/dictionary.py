# list1=['Five',5,'Six',6,"Seven",7,"Seven",8,"Nine",9]
# '''keys=[]
# values=[]'''
# dict1={}
# '''for i in list1:
#     if type(i)==str:
#         keys.append(i)
#     else:
#         values.append(i)
# for k in range(0,len(values)):
#     if keys[k] in dict1:
#         l=dict1.get(keys[k])
#         dict1[keys[k]]=[l,values[k]]
#     else:
#         dict1[keys[k]]=values[k]
# print(dict1)'''
#
# for k in range(0,len(list1),2):
#     if list1[k] in dict1:
#         #l=dict1.get(list1[k])
#         #dict1[list1[k]]=[dict1.get(list1[k]),list1[k+1]]
#         dict1[list1[k]] = [dict1[list1[k]], list1[k + 1]]
#     else:
#         dict1[list1[k]]=list1[k+1]
# print(dict1)

str="This is a pycharm ide project jayashr"
list1=str.split()
dict1={}
for i in list1:
    if len(i) not in dict1:
        dict1[len(i)]=i
    else:
        dict1[len(i)]=[dict1[len(i)],i]
print(dict1)

for i in dict1:
     if type(dict1[i])==list:
        print(dict1[i])
