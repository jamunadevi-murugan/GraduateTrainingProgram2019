def rotate_word(string,integer):
    ascii=[]
    rotated=[]
    rotate=[]
    for i in range(0,len(string)):
        ascii.append(ord(string[i]))
    for j in range(0,len(ascii)):
        rotating=ascii[j]+integer
        rotated.append(rotating)
    for k in range(0,len(rotated)):
        if(rotated[k]>=97 and rotated[k]<=122):
            rotate.append(chr(rotated[k]))
        elif rotated[k]<97:
            excess=96-rotated[k]
            actual=122-excess
            rotate.append(chr(actual))
        else:
            excess=rotated[k]-122
            actual=96+excess
            rotate.append(chr(actual))
    rotated_string=''.join(rotate)
    return rotated_string

string=input("Enter a string to rotate : ")
integer=int(input("Enter the integer : "))
print(rotate_word(string,integer))
