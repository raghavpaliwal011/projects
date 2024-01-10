print("welcome to my game")
score=0

QUESTION = input ("do you want to play ? ")
print(QUESTION)
if QUESTION != "yes":
    quit()

else :
    print("lets play")

q1 = input ("question 1/ what is the biggest fandom in the world ? ")
if q1 !=  "bts army":
    print("retry next time")
    
else:
    print("right , now next question")
    score += 1

q2 =input("question2/ coldest place on earth ? ")
if q2 != "antarctica":
    print("wrong answer you dumb:<")

else:
    print("right , now next question")
    score += 2

q3 = input("question3/ who is the prime minister of india ? ")
if q3 != "MR NARENDRA MODI":
    print(q3.upper)
    print("why,why,why? :<")

else:
    print("right , now next question")
    score += 3

q4= input("question4/ which is the tallest building in the world ? ")
if q4 != "burj khalifa":
    print("how dumb you are")

else:
    print("right , now next question")
    score += 4

q5 = input ("most selling artists")
if q5 != "bts":
    print("i give you another chance")
    input("options are : bts,the weekend,txt : ")

else:
    print("right , now next question")
    score += 5