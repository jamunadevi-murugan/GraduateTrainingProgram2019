def has_no_e(word):
    word1=word.lower()
    count=0
    for i in range(0,len(word1)):
        if word1[i]=='e':
            count=count+1
    if count==0:
        return False
    else:
        return True
word=input("Enter a word to find whether the word has e or not : ")
print(has_no_e(word))