def is_prime(number):
    prime = 0
    for i in range(2, number):
        if number % i == 0:
            prime = 1

    if prime == 0:
        print("Number %d is a prime" % number)
    else:
        print("Number %d is not a prime" %number)

game = 1

while game == 1:
    try:
        number_to_check = int(input("\nEnter a number: "))
    except ValueError:
        print("That's not a number")
        continue

    is_prime(number_to_check)

    again = input("\nEnter 'q' to exit or anything else to try again: ")

    if again == "q":
        game = 0
        print("Goodbye!")