import sys
'''print("Name of the file is ",sys.argv[0])
a=sys.argv[1]
b=sys.argv[2]
c=a+b
print(a,b)
print(eval(c))'''

import sys
try:
    a=sys.argv[1]
    b=sys.argv[2]
    c=sys.argv[3]
    max=0
    for i in range(1,len(sys.argv)):
        if max<int(sys.argv[i]):
            max=int(sys.argv[i])
    print(max)
except Exception:
    print("Not sufficient values")

'''list1=sys.argv
list1.remove(sys.argv[0])
print(list1)
print(max(list1))'''