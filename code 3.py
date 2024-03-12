# whatever thing i have made it just explains self function :}
class saiyan:
    def goku_details(self):
        return f"name is {self.name} universe is {self.universe}"

    def vegeta_details(self):
        return f"name is {self.name} universe is {self.universe}"
    
goku = saiyan()
vegeta = saiyan()

goku.name="goku"
goku.universe="7th"

vegeta.name = "vegeta"
vegeta.universe = "7th"

print (goku.goku_details())
print (vegeta.vegeta_details())
