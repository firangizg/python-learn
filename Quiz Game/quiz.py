print("Welcome to the quiz!")

startGame = input("Do you want to play the game? (yes/no) ")

if startGame.lower() != "yes":
    quit()

print("Okay, let's begin the quiz game! \n")

score = 0

question = input("What does CPU stand for? ")
if question.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

question = input("What does GPU stand for? ")
if question.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

question = input("What does RAM stand for? ")
if question.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

question = input("What does PSU stand for? ")
if question.lower() == "power supply":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print("\nYou got " + str(score) + " questions right! You got " + str((score / 4) * 100) + "%")
