# import csv
# with open("csv_read.csv") as file1:
#     read=csv.reader(file1)
#     for i in read:
#         print(i)
#
# with open("csv_write.csv",'w') as file2:
#     write=csv.writer(file2,delimiter=',')
#     write.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# import csv
# with open("csv_read.csv") as file3:
#     dictread=csv.DictReader(file3)
#     for i in dictread:
#         print(i)

import csv
with open('csv_write_dict.csv','w') as file4:
    fieldname=['first_name','last_name']
    writer=csv.DictWriter(file4,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
