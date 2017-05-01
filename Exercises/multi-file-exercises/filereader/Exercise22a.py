import os, re

# test1.txt and sun.txt are files linked to this exercise

found = 0

while found == 0:
    try:
        # DO NOT GIVE FILE EXTENSION HERE, CURRENTLY SUPPORTS ONLY .TXT
        filename = input("\nWhat file (.txt) would you like to read: ")
        open(filename + ".txt")
        found = 1
    except FileNotFoundError:
        print("File not found.")
        continue

# Making the filename (and making it to be a .txt)
filename = "_".join(filename.split()) + ".txt"


# Making a function for checking if file exits
def f_exist(filename):
    return os.path.isfile(filename)

if filename != "sun.txt":
    with open(filename, 'r') as f:
        content = f.readlines()
        f.close()

    # Removing newlines
    content = [x.strip() for x in content]

    # Printing content, but opting sun.txt out because we will work that afterwards..
    for i in content:
        print(i)

    # Name statistics for test1.txt

    namecount = {}

    for i in set(content):
            namecount[i] = content.count(i)

    print("\nThe force was strong with these one: ")
    for key in namecount:
        print(str(namecount[key]) +" times " + key)

# Starting to work out categories in sun.txt
if filename == "sun.txt":
    with open(filename, 'r') as f:
        content = f.readlines()
        f.close()

    categories = []

    for i in content:
        tmp = re.split("/", i)
        categories.append(tmp[2])

    print("\nThere were these categories in file sun.txt: \n")
    for i in sorted(set(categories)):
        print(i)
