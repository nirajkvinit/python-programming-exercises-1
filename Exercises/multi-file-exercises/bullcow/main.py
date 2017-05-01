import randomer, counter

s_number = randomer.makerandom()
answer = 0
guesses = 0

print("\nWelcome to the Cows and Bulls game!\n")
print("\n%d\n" % s_number)


while answer != s_number:
    try:
        answer = int(input("Enter a number between 1000 and 9999: "))
        if answer < 1000 or answer > 9999:
            print("\nThe number you entered isn't between 1000-9999!\n")
            continue
    except ValueError or TypeError:
        continue

    guesses += 1

    if answer != s_number:
        print("%d cows, %d bulls" % ((counter.cows_and_bulls(answer, s_number)[0]), counter.cows_and_bulls(answer, s_number)[1]))
        continue
    else:
        print("\nCongratulations! Guess number %d was the right one." % guesses)

