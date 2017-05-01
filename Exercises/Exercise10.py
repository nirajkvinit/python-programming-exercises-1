#Create lists

list1 = []
end_list1 = 0

while end_list1 == 0:
    new_number = input("Please enter a number you want to add to list 1 or press [enter] to continue: ")

    if new_number == "":
        end_list1 = 1
    else:
        try:
            list1.append(int(new_number))
        except ValueError:
            print("That's not a number")
            continue

list2 = []
end_list2 = 0

while end_list2 == 0:
    new_number = input("Please enter a number you want to add to list 2 or press [enter] to continue: ")

    if new_number == "":
        end_list2 = 1
    else:
        try:
            list2.append(int(new_number))
        except ValueError:
            print("That's not a number")
            continue

print("\nCommon items in these two lists are: %s" % (list(set(list1).intersection(list2))))