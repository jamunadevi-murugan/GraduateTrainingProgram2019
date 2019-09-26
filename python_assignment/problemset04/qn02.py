class Person:
    def getGender(self):
        print("Person class")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

gender=input("Enter the gender : ")
gender=gender.lower()
if gender=='m' or gender=='male':
    x=Male()
    x.getGender()
else:
    y=Female()
    y.getGender()