'''import math
binary_number=input("Enter the binary number : ")
decimal_number=0
binary_list=list(binary_number)
"""print(bin(20).replace("0b",""))
print(15//4)
def d(num):
    if num>1:
        d(num//2)
    print(num%2,end='')
d(20)"""
print(binary_list)
length=len(binary_list)-1
for i in range(0,len(binary_list)):
        power=pow(2,length)
        #print(binary_list[i])
        binary_list[i]=int(binary_list[i])*power
        #print(binary_list[i])
        length=length-1
sum=0
for j in range(0,len(binary_list)):
    sum=sum+int(binary_list[j])
print("Decimal Equivalent of the binary number 10011 is ",sum)'''

bn=int(input("Enter the binary number : "))
temp=bn
dn=0
rem=0
p=0
while(bn!=0):
    rem = bn % 10
    bn=bn//10
    power=pow(2,p)
    dn=dn+(rem*power)
    p=p+1
print("The decimal equivalent of the binary number ",temp," is ",dn)