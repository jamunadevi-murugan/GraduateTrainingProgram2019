def is_abecedarian(string):
    string=string.lower()
    for i in range(0,len(string)):
        for j in range(i+1,len(string)):
            if string[i]>string[j]:
                return False
    return True

string=input("Enter a string : ")
print(is_abecedarian(string))