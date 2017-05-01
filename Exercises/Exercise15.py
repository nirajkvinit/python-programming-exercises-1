def reverse(sentence):
    return " ".join(sentence.split()[::-1])

print("\nI'm gonna reverse whatever you enter to me!")
r = input("Enter a thing you want to be reversed: ")

if "marriage" in r.lower():
    print("\nGo to couples therapy and sort that thing out")
elif "child" in r.lower():
    print("\nNope, not gonna reverse that. Time for you to grow up.")
elif "death" in r.lower():
    print("\nNo one can reverse that. Live with it.")
elif "skyrim" in r.lower():
    print("\nBelieve me, I miss the first playthrough too..")
else:
    print("\nBoom! %s reversed is: '%s'" % (r, reverse(r)))