# import re
#
# str_password=input("Enter the passwords with comma seperated values : ")
# list_password=str_password.split(",")
# for i in range(0,len(list_password)):
#     if len(list_password[i])>=6 and len(list_password[i])<=12:
#         a=re.findall("[a-z]",list_password[i])
#         if len(a)>=1:
#             a=re.findall("[A-Z]",list_password[i])
#             if len(a)>=1:
#                 a = re.findall("[0-9]", list_password[i])
#                 if len(a)>=1:
#                     a=re.findall("[$#@]",list_password[i])
#                     if len(a)>=1:
#                         print(list_password[i])


# string="The quick brown fox jumps over the lazy dog"
# string=string.lower()
# string_list=string.split(" ")
# string_str=''.join(string_list)
# set1=set(string_str)
# if len(set1)==26:
# 	print("Pangram")
# else:
# 	print("Not a Pangram")

f1=open("file1.txt","r")
file_list=f1.readlines()
print(len(file_list))

# sample_items=input()
# items_list=sample_items.split('-')
# items_list.sort()
# print('-'.join(items_list))

# sample_list=[1,2,3,3,3,4,5]
# unique_list=[]
# for i in sample_list:
# 	if i not in unique_list:
# 		unique_list.append(i)
# print("Unique List : ",unique_list)

# import re
# string=input("Sample String : ")
# upper=re.findall("[A-Z]",string)
# lower=re.findall("[a-z]",string)
# print("No. of Upper case Characters : ",len(upper))
# print("No. of Lower case Characters : ",len(lower))

f1=open("file1.txt","r")
f2=open("file2.txt","r")
file_list1=f1.readlines()
file_list2=f2.readlines()
new_file1=[]
for i in range(0,len(file_list1)):
		list1=list(file_list1[i])
		list2=list(file_list2[i])
		if '\n' in list1:
			list1.remove('\n')
		new_file1.append(''.join(list1)+''.join(list2))
for i in new_file1:
    print(i)

f1=open("file1.txt","r")
f2=open("file2.txt","r")
file_list1=f1.readlines()
file_list2=f2.readlines()
new_file1=[]
for i in range(0,len(file_list1)):
		new_file1.append(file_list1[i].strip()+file_list2[i].strip())
for i in new_file1:
    print(i)

# import re
# str = "The rain in Spain"
# x = re.search("\s", str)
# print("The first white-space character is located in position:", x.start())

