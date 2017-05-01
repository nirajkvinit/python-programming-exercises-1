# Asking user input
my_string = input("\nPlease enter a string: ")

# Defining check function


def palindrome_check(a_string):
    my_list = [i.lower() for i in a_string]
    backwards_list = []

    for x in range(0, len(my_list)):
        backwards_list.append(my_list[(len(my_list) - 1 - x)])

    if compare_lists(my_list, backwards_list):
        return ("%s is a palindrome" % my_string)
    else:
        return ("%s is not a palindrome" % my_string)


def compare_lists(a, b):

    true = 1

    for x in range(0, len(a)):
        if(a[x] == b[x]):
            continue
        else:
            true = 0
            break

    if(true == 1):
        return True
    else:
        return False

print(palindrome_check(my_string))


print("\n\n*******Simpler solution*******")

def simple_check(a):
    my_list = [i.lower() for i in a]
    if (my_list == my_list[::-1]):
        return True
    else:
        return False

print("I assume that %s a palindrome and that assumption is: %r" % (my_string, simple_check(my_string)))