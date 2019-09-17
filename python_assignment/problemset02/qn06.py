def findAnEven(l):
    try:
        for i in l:
            if i % 2 == 0:
                return i
        raise ValueError()
    except ValueError:
        return "No Even numbers in list!"
list1=[]
num=int(input("Enter number of values : "))
for i in range(0,num):
    a=int(input())
    list1.append(a)
print(findAnEven(list1))