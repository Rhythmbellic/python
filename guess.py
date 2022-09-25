import random
randnumber=random.randint(1,100)
def fuck():
    userGuess=None
    while (randnumber!=userGuess):
        userGuess=int(input("Enter your guess\n"))
        if(randnumber<userGuess):
            print("your number is greater\n")
            guesses += 1
        elif(randnumber==userGuess):
            print("you have guessed right\n")
            print(f"In {guesses} Guesses")
        else:
            print("your number is smaller\n")
            guesses += 1
fuck()