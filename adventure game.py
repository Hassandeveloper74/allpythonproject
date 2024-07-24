name = input("what is your name :")
print("Welcome ", name,"To This Adventure")

answer=input("You're on a Dirt Road,It has to come to an end and you can go left and right.Which would you like to go ?").lower()

if answer=="left":
    answer=input("You come to the river, you can walk around or swim across  (walk\swim)").lower()
    if answer=="swim":
        print("You swim across and were eaten by elegant")
    elif answer=="walk":
        print("you walked many miles,ran out of water and lost the game")
    else:
        print("Not a Valid opton.You  Lose!")


elif answer=="right":
    answer=input("You come to a bridg,Its looks wobbly do you want to crosss it or head back (cross/back) ? ").lower()
    if answer=="back":
        print("You go back and lose")
    elif answer=="cross":
        answer=input("You cross the brigde and meet a stranger.Do u talk to  them (yes/no) ").lower()
        if answer=="yes":
           print("you talk the stranger and they give you gold you WIN!")
        elif answer=="no":
            print("you ignore the stranger and they are affended and You Lose!")

        else:
           print("Not a Valid opton.You  Lose!")

    else:
        print("Not a Valid opton.You  Lose!")

else:
    print("Not a valid option")

print("thank you for trying.", name)