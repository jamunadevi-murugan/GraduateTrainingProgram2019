import math
list1={}
integer=int(input("Enter an integer value : "))
for power in range(1,6):
    int1=integer**(1/power)
    if math.ceil(int1)==int1:
        list1[int1]=power
if len(list1)!=0:
    for i in list1:
        print(i,list1[i])
else:
    print("No pairs")
   #print(math.ceil(int1),int1)