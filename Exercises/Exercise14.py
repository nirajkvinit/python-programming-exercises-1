def no_duplicates(list):
    return set(list)

def no_duplications(list):
    a = []
    for i in list:
        if i not in a:
            a.append(i)
    return a

a = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 11]

print("method one: " + str(no_duplicates(a)))
print("method two: " + str(no_duplications(a)))
