print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Maybe next time!")
    quit()

print("Great! Let's get started.")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Central Processing Unit.")  



answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:   
    print("Incorrect! The correct answer is Graphics Processing Unit.") 


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":    
    print("Correct!")
    score += 1

else:
    print("Incorrect! The correct answer is Random Access Memory.")


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":    
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Power Supply Unit.")    



print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")



