def avoid(word,forbidden_string):
    for i in word:
        if i in forbidden_string:
            return False
    return True
word=input("Enter the word : ")
forbidden_string=input("Enter a forbidden letters : ")
print(avoid(word,forbidden_string))