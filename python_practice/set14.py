import math
radius=int(input("Enter radius value : "))
volume=(4/3)*(math.pi*math.pow(radius,3))
print("The volume of a sphere :","{:.2f}".format(volume))

a_price=24.95*60
percent=a_price*(40/100)
c_price=a_price-percent
d_price=0
print(c_price)
for i in range(1,61):
    if i==1:
        d_price=d_price+3
    else:
        d_price=d_price+0.75
print(d_price)
s_price=c_price+d_price
print("Price is : ",s_price)

'''a_price=float(input("Enter cover price of a book : "))
p=int(input("Enter discount percentage : "))
percent=a_price*(p/100)
#c_price=a_price-percent
copies=int(input("Enter how many copies : "))
a_price=a_price*copies
d_price=0
#print(c_price)
for i in range(1,copies+1):
    if i==1:
        d_price=d_price+3
    else:
        d_price=d_price+0.75
#print(d_price)
s_price=a_price+d_price
c_price=s_price-percent
print("Price is : ",c_price)'''

current_hours = 6
current_minutes = 52
easy_pace_minutes = 8
easy_pace_seconds = 15
tempo_pace_minutes = 7
tempo_pace_seconds = 12
easy_miles = 2
tempo_miles = 3

easy_time = (easy_pace_minutes * 60 + easy_pace_seconds) * easy_miles
#print(easy_time)
tempo_time = (tempo_pace_minutes * 60 + tempo_pace_seconds) * tempo_miles
#print(tempo_time)
run_time = easy_time + tempo_time
#print(run_time)
current_time = current_hours * 3600 + current_minutes * 60
#print(current_time)
end_time = current_time + run_time
#print(end_time)
end_hours = end_time // 3600
#print(end_hours)
end_minutes = (end_time % 3600) // 60
#print(end_minutes)
end_seconds=(end_time % 3600) % 60
#print(end_seconds)
print("I will go home for breakfast at ",end_hours,":",end_minutes,":",end_seconds," am")



