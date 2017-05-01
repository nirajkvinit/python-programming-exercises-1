num = int(input("Enter a number: "))
divisors_list = []


if (num >= 1):
    for x in range(1, num + 1):
        if (num % x == 0):
            divisors_list.append(x)
    print(divisors_list)
else:
    print("No positive divisors for number %d" % num)