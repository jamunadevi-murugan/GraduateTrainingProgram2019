x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
z=int(input("Enter z value:"))
list1=[]
if x%2!=0:
    list1.append(x)
if y%2!=0:
    list1.append(y)
if z%2!=0:
    list1.append(z)
#print(list1)
maxi=0
if len(list1)==0:
    print("None of them are odd")
else:
    for i in range(0,len(list1)):
        if list1[i]>maxi:
            maxi=list1[i]
print("Largest element is :",maxi)
