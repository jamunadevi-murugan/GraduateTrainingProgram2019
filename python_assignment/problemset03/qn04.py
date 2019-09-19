def has_no_e(word):
    string=''
    list_has_no_e=[]
    for i in range(0,len(word)):
        string=word[i]
        string=string.lower()
        if 'e' not in string:
            list_has_no_e.append(string)
    return list_has_no_e
input_string=input("Enter a list of words separated by space ")
word=input_string.split(" ")
list_has_no_e=[]
list_has_no_e=has_no_e(word)
print(list_has_no_e)
length1=len(word)
length2=len(list_has_no_e)
percentage=(length2/length1)*100
print(percentage)