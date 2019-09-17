import re
string="Hakka and Bukka were brothers and warriors. The brothers wanted to build their own kingdom where people could live without fear. They collected a band of young men and trained them in warfare. They lived in a forest hideout on the banks of the river Tungabhadra in South India.\
One day, the brothers were out on a hunt. Ferocious dogs accompanied them. They crossed the river and rode on. A couple of frightened rabbits ran out of the bushes. The dogs gave them chase with the two brothers closely behind on their horses. \
It was a long chase. The rabbits were running for their life. The dogs were catching up. Suddenly, in a swift move, the rabbits turned and faced the dogs. Taken aback by the show of defiance, the barking dogs stepped back. Hakka called back the dogs. As the dogs turned back, the rabbits walked away.\
Hakka looked around. They were on the other side of the Tungabhadra. It was a rocky land. The sun was blazing in the sky.\
 “Strange! I’ve never seen rabbits challenging dogs before!” said Bukka.\
“That’s the quality of this land,” said a quiet voice, “Even rabbits give fight.”\
Startled to hear a stranger speak, the two brothers turned.\
They saw a holy man walking towards them. He was a picture of peace. At the same time, his eyes were blazing bright."
total_dictionary={}
list_max_word=[]
dictionary_word={}
length_of_string=len(string)
#print(length_of_string)
string_lower=string.lower()
word_list=re.findall("\w+",string_lower)
word_count=len(word_list)
maximum_count=0
#print(word_list)
#print(word_count)
for i in range(0,len(word_list)):
    count=word_list.count(word_list[i])
    dictionary_word[word_list[i]]=count
for j in dictionary_word:
    if dictionary_word[j]>maximum_count:
        maximum_count=dictionary_word[j]
#print(maximum_count)
for k in dictionary_word:
    if maximum_count==dictionary_word[k]:
        list_max_word.append(k)
#print(list_max_word)
repeated_word_count=0
repeated_word_list=[]
for l in dictionary_word:
    if dictionary_word[l]>=2:
        repeated_word_count=repeated_word_count+1
        repeated_word_list.append(l)
#print(repeated_word_count)
#print(repeated_word_list)
total_dictionary["length_of_string"]=length_of_string
total_dictionary["Number of words"]=word_count
total_dictionary["Max occurance"]=maximum_count
total_dictionary["Max occurance word"]=list_max_word
total_dictionary["Repeated word's count"]=repeated_word_count
total_dictionary["Repeated word's list"]=repeated_word_list
print(total_dictionary)