class saiyan:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showdetails(self):
        print (f"name is {self.name} id is {self.id}")

class earthling(saiyan):
    def planet(self):
        print ("planet is vegeta")
e1 = saiyan("bardock",45)
e1.showdetails()
e2 = earthling("goku",10000000000000000000000000000000000000000)
e2.showdetails()
e2.planet()