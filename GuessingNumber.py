import random

MINIMUM = 1
MAXIMUM = 9

randomNumber = random.randint(MINIMUM, MAXIMUM)
i = 0


def ifstatement():
    while True:
        anotherRound = str(input("Continue guessing? 'y' for continue, otherwise enter 'exit': "))
        if anotherRound == "y":
            break
        elif anotherRound == "exit":
            # print("You got it right! It only took you " + str(iteration) + "tries!")
            exit()
        else:
            print("Wrong input!")
            continue


while True:
    guessNumber = int(input("Please enter a number between 1~9: "))
    if guessNumber < randomNumber:
        print("The number you entered is too low.")
        i += 1
        ifstatement()

    elif guessNumber > randomNumber:
        print("The number you entered is too high.")
        i += 1
        ifstatement()

    else:
        print("The number you entered is equal to the random number!")
        i += 1
        print("You got it right! It only took you " + str(i) + " tries!")
        break
