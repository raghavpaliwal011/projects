#here suppose this code is of 1000 lines and someone comes and says that you need to change this class , will you change it obviously not .And if you do so then you will face error in every line of the programme where this class is used instead of changing it we will use inheritance as shown below
class employyee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showdetails (self):
        print (f"the name of the employee : {self.id} is {self.name}")

#from here the inheritance starts

class programmer(employyee): # in easy language programmers father is employee and programmer has got many habits from his father and showlanguage is its own habit which his father dont have
    def showlanguage(self):
        print ("the language is python")

e1 = employyee("rohan das ", 410)
e1.showdetails()
e2 = programmer("raghav",4100)
e2.showdetails()
e2.showlanguage

