import math
input1=input("Enter comma seperated binary values : ")
binary_list=input1.split(",")
decimal_list=[]
for i in binary_list:
    binary=i
    a=0
    decimal=0
    for j in range(len(binary)-1,-1,-1):
        decimal=decimal+(float(binary[j])*math.pow(2,a))
        a=a+1
    decimal_list.append(decimal)
dict_btd={}
for i in range(0,len(binary_list)):
    dict_btd[binary_list[i]]=decimal_list[i]
for i in dict_btd:
    if dict_btd[i]%5==0:
        print(i)