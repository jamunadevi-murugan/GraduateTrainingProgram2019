def avoids(word_list,forbidden_string):
   resultant_words=[]
   for i in word_list:
      word=i
      count=0
      for j in word:
         if j in forbidden_string:
            count=count+1
      if count==0:
         resultant_words.append(word)
   length=len(resultant_words)
   minimum=len(resultant_words[0])
   combination_list=[]
   for k in range(0,len(resultant_words)):
      len1=len(resultant_words[k])
      if minimum>len1:
         minimum=len1
   for l in resultant_words:
      if len(l)!=minimum:
         combination_list.append(l)
   return length,combination_list
word_string=input("Enter the list of words seperated by space : ")
word_list=word_string.split(" ")
forbidden_string=input("Enter the forbidden letters : ")
count,smallest_string=avoids(word_list,forbidden_string)
print("The number of words that don't contain any of the forbidden letters is ",count)
print("Combination of forbidden letters that excludes the smallest number of words is ",len(smallest_string))