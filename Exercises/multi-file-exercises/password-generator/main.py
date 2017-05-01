import password, time

running = 1

print("\nHi and welcome to the password generator!\n")

while running:
    choice = 4
    passwrd = ""

    while choice < 0 or choice > 2:
        try:
            choice = int(input("Would you like to have a easy(0), medium(1) or strong(2) password: "))
        except ValueError:
            continue

    if choice == 0:
        passwrd = password.generate_password("easy")
    elif choice == 1:
        passwrd = password.generate_password("medium")
    else:
        passwrd = password.generate_password("strong")

    print("\nYour new password is: %s\n" % passwrd)

    again = input("Would you like to generate a new password (y/n): ")

    if again == "n":
        running = 0
    elif again == "y":
        continue
    else:
        for i in range(3):
            print("...")
            time.sleep(1)
        print("You didn't answer yes (y) or no (n)..")
        time.sleep(1)
        for i in range(3):
            print("...")
            time.sleep(1)
        time.sleep(1)
        print("\n\nWhen you can't understand - you can always assume. Lets generate a new password for you!\n\n")
        time.sleep(3)