#adventure 

name = input ("type your name : ")
print ("namaste",name)
question=input("do you want to come to my adventure ?")

if question == "yes":
    print ("then you are most welcome to the adventure :>")

else:
    print ("then you can leave :<")
    quit()

path = input ("you are going from a way on road , you see three paths first has snakes second has fire and third has lions who are hungry from a couple of months wich way will you go ? write(1 to go on first path , 2 for second and 3 for third)")
if path == "1":
    print("you got bitten by snakes and died")

elif path == "2":
    print ("you got burnt in the fire")

elif path =="3":
    print ("lions were hungry from a couple of months and no one can live this long without food,so you got it right :>")

else:
    quit()

CHOICE1 = input ("you have crossed the lions and now you are given a car and a bike which one will you choose write(1 for bike and 2 for car)")
if CHOICE1 == "1":
    print ("there will be some problems in next path but it will be ok")

elif CHOICE1 == "2":
    print ("you will be safe on next path")

else:
    quit()

choice2 = input ("now you have come to an auditorium and there is blood everywhere you get scared and you get out of the auditorium and get to your vehicle and started moving and then out of nowhere some zombies come if you had taken a car you are safe quite a bit and you can run or you can switch to bike write (b for bike and c to stay on car and run )")
if choice2 == "b":
    print ("this was not a good decision :<")
elif choice2  == "c":
    print ("ok but zombies will return :>")

question = input("now you have come to an auditorium and there is blood everywhere you get scared and you get out of the auditorium and get to your vehicle and started moving and then out of nowhere some zombies come and now if you have taken bike it will be bad for you but you can run or you can quit write (r to run and q to quit)")

if question == "r":
    print ("now another choice ")

elif question == "q":
    quit()

else:
    quit()

choice3 = input ("now you are given one one chance to take helicopter or a bike or a car press (h for helicopter , b for bike and c for car)")
if choice3 == "w":
    print("ok not bad but it can be a little harder but you will be safe now")