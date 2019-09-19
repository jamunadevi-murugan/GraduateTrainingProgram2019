def is_sorted(element_list):
    list1=element_list
    count=0
    maximum=0
    for i in range(0,len(list1)):
        if list1[i].isdigit():
            list1[i]=int(list1[i])
            count=count+1
    if(count==len(list1)):
        for j in range(0, len(list1)):
            for k in range(i + 1, len(list1)):
                if list1[j]>list1[k]:
                    return False
    if(count==0):
        for j in range(0, len(list1)):
            for k in range(j + 1, len(list1)):
                if list1[j]>list1[k]:
                    return False
    return True
string=input("Enter a list of elements seperated by space : ")
list1=string.split(" ")
print(is_sorted(list1))