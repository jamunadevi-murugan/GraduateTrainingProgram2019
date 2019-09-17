str1='ds1d'
str2='ssd1'
count=0
print(sorted(str1))
s1=sorted(str1)
s2=sorted(str2)
if len(str1)==len(str2):
        if s1== s2:
            print("Anagram")
        else:
            print("Not Anagram")