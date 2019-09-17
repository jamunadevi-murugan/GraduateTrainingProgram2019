s=str(input("Enter a set of decimal numbers seperated by comma:"))
list1=s.split(",")
sum=0
print(list1)
for i in range(0,len(list1)):
    sum=sum+float(list1[i]);
print("The sum of given numbers is ",sum)