def game():
    answer = input("Would you like to play the game?(y/n)")
    if answer.lower() == 'y':
        print("Welcome to the game")
        answer = input("You reach a crossroads, would you like to go left or right?").lower()
        if answer == "left":
            answer = input("You encounter a monster, would you like to run or attack.").lower()
            if answer == "attack":
                print("This wasn't great idea you lost!")
            else:
                print("Good choice, you made it away safely")
                answer = input("You see a car and plane. Which one would you like to take?")
                if answer == "car":
                    print("you won")
                elif answer == "plane":
                    print("You don't know how to fly you loose")
        elif answer == "right":
            print("you walk aimlessly to right and fall down. You injure your leg")
        else:
            print("Invalid choice")
    else:
        print("Okay, some other time")

game()
