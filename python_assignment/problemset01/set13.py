list1=[]
list2=[]
input("Enter 10 integer : ")
for i in range(1,11):
    a=int(input())
    list1.append(a)
#print(list1)
for j in list1:
    if j%2!=0:
        list2.append(j)
#print(list2)
if len(list2)==0:
    print("No Odd Number was entered!!")
else:
    print("Largest Odd Number is : ",max(list2))