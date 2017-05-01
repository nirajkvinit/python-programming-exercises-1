import random, time

game = 1
count = 0

while game == 1:
    randnumber = random.randint(1,9)

    print("\nWelcome to the guessing game!")

    time.sleep(1)

    play = input("Say 'exit' to quit or press [enter] to start a new game: ")

    guess = -1

    if play == "exit":
        break
    else:
        while guess < 1 or guess > 9:
            try:
                guess = int(input("\nGuess a number between [1-9]: "))
            except ValueError:
                continue

        time.sleep(1)
        if randnumber == guess:
            print("\nCongratulations! The right number was %d." % randnumber)
            count += 1
        else:
            print("\nYou guessed wrong! The right answer would have been %d." % randnumber)
            count += 1

        time.sleep(2)

print("\nYou played the guessing game %d times" % count)