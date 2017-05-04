# Guessing game

import random

not_ok = 1
num = 0

while not_ok:
    try:
        num = int(input("Give me a number between 0 and 100: "))
        print("\n")

        if -1 < num < 101:
            not_ok = 0
        else:
            print("BETWEEN 0 AND 100 I SAID!\n")
    except ValueError:
        continue

guess = random.randint(0, 100)
top = 100
bottom = 0
guess_count = 1


while guess != num:

    cheating = 1

    while cheating:
        pro_tip = input("My guess is %d, tell me is it too high or low: " % guess).lower()
        if pro_tip != "high" and pro_tip != "low":
            print("Hey, I can't understand what you're saying! Tell me if my guess was too 'high' or 'low'.\n")
        elif (guess < num and pro_tip == "high") or (guess > num and pro_tip == "low"):
            print("Hey, don't try to fool me! Cheaters are going to banned and you wouldn't want that to happen..\n")
        else:
            cheating = 0

    if pro_tip == "low" and guess > bottom:
        bottom = guess

    elif pro_tip == "high" and guess < top:
        top = guess


    print("Okay, well..\n")
    guess = random.randint((bottom + 1), (top - 1))
    guess_count += 1

print("\nCongratulations to me! I'm the winner! I did it with %d guesses!\nBut for real, I always knew the number would be %d.." % (guess_count, num))