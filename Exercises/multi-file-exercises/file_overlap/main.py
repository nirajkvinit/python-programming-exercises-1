
f1 = open('happynumbers.txt', 'r')
f2 = open('primenumbers.txt', 'r')

c1 = f1.read().splitlines()
c2 = f2.read().splitlines()

f1.close()
f2.close()

overlap = list(set(c1).intersection(c2))

# Uncomment if you want to print overlapping numbers
# for i in overlap:
    # print(i)
