a=1
b=5
for num in range(a,b+1):
    count=0
    if num>1:
        for i in range(2,num):
            if num%i==0:
                count=1
                break
        if(count==0):
            print(num)