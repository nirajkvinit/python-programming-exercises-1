def less_than_ten(a, b):
    return([i for i in a if i < b])

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Enter a number: "))

print(less_than_ten(a, num))