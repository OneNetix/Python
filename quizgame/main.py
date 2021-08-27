playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does SOC stand for? ")
if answer.lower() == "system on chip":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

if score == 4:
    print("AMAZING you got full marks your percentage was " + str(score/4 * 100) + "%")
    print("Your score = " + str(score) + " out of 4 questions correct!")
else:
    print("Your score = " + str(score) + " out of 4 questions correct!")
    print("That was " + str(score/4 * 100) + "% correct!")