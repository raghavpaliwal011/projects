print ("enter number 1")
num1 = input()
print ("enter number 2")
num2 = input()
try: # this function in python tries to execute a certain line and even if it dosent works , it will not show error instead it will leave that line and run the other line
    print ("the sum of number 1 and number 2 is",
           int(num1)+int(num2))
except Exception as e: # this function will not let the error to stop the programme. this will print the exception as a string
    print (e)
print ("this line is very important")