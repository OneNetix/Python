name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across? Type swim to swim or walk to walk around it: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by a shark.")
    elif answer == "walk":
        print("You walked for many miles and ran out of water and you died.")
    else:
        print("Not a valid option you loose!")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ").lower()

    if answer == "cross":
        answer = input("You crossed the bridge and meet a stranger, do you talk to them (Yes/No) ").lower()
        if answer == "yes":
            print("You talked to the stranger and they gave you gold, you won!!!!!")
        elif answer == "no":
            print("You ignored them, that was rude they kill you!")
        else:
            print("Not a valid option you loose!")
    elif answer == "back":
        print("You go to the back to the road and get lost, you died after days of walking around.")
    else:
        print("Not a valid option you loose!")


else:
    print("Not a valid option you loose!")

print("Thank you for playing", name, "hope you enjoyed")