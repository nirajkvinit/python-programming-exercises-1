num1 = int(input("Please enter number you want to divide: "))
num2 = int(input("Please enter the divider: "))

if (num1 % num2 == 0):
    print("%d divides evenly into %d" % (num1, num2))
else:
    print("%d doesn't divide evenly into %d" % (num1, num2))

