def getRatios(vect1,vect2):
    list1=[]
    for i in range(0,len(vect1)):
        try:
            c=vect1[i]/vect2[i]
            list1.append(c)
        except Exception as err:
            print(err)
    return list1
list2=[1,2,3,4,5]
list3=[6,7,8,0,2]
l=getRatios(list2,list3)
print(l)