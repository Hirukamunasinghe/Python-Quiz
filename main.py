playing = input ("Do you want to play this game? ")
if playing.lower() != "yes" : 
    quit()
else : 
    print("Welcome to the quiz :)")
    score = 0
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory" : 
    score += 1 
    print("Correct answer")
else : 
    print("Incorrect answer")
answer = input ("What does GPU stand for? ")
if answer.lower() == "graphics processing unit" : 
    score += 1
    print ("Correct answer")
else : 
    print ("Wrong answer")
answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output system" : 
    score += 2
    print("Correct answer")
else : 
    print ("Wrong answer")
print(f"Your total score for this quiz is {score} / 4")

    