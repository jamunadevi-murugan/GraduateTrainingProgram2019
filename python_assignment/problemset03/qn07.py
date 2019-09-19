def using_only(word,string):
    word=list(filter(lambda b: b != ' ', word))
    dec_list=list(map(lambda a:a in string,word))
    count=0
    for i in dec_list:
        if i==True:
            count=count+1
    if(count==len(word)):
        return True
    else:
        return False
word=input("Enter a word : ")
string=input("Enter a string of letters : ")
print(using_only(word,string))