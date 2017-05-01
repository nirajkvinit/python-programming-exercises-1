#Import for random lists
import random

#List variables
a = []
b = []

#Creating two random lists with length of 100
for i in range(0, 101):
    a.append(random.randint(0,1001))
    b.append(random.randint(0,1001))

#Defining function for getting numbers two lists have in common
def common_items(a, b):
    answer = []
    for i in set(a):
        if i in b:
            answer.append(i)
    return answer

#Storing result to a variable for later usage
result = common_items(a, b)

#Printing out the result and count of common items
print("\nLists have %d items in common and they are: " % len(result))
print(sorted(result))



print("\n\n***** With oneliner *****")


#Oneliner solution for problem

def oneliner (a, b):
    return [i for i in set(a) if i in b]

#Printing oneliner
print(sorted(oneliner(a, b)))
