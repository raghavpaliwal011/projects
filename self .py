class employee:
    def print_details(self):
     return f"name is {self.name} salary is {self.salary} role is {self.role}"
suui = employee()
suui.name = "suui"
suui.salary = "5555"
suui.role = "manager"

print (suui.print_details())