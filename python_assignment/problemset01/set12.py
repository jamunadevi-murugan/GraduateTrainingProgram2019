def right_justify(s):
    #count=0
    for j in range(0,(70-len(s))):
        #count=count+1
        print(end=" ")
    print(s)
    # print(s.rjust(i))
    #print(count)
name=str(input("Enter a String : "))
right_justify(name)