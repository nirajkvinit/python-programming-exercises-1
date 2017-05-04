# Making a game board

not_ok = 1

while not_ok:
    try:
        x = int(input("What size game board you want to draw: "))
        not_ok = 0
    except ValueError:
        continue

v_cell = " --- "
h_cell = "|   |"

b_width = v_cell * x
c_edge = h_cell * x


for i in range(x):
    print(b_width)
    print(c_edge)
print(b_width)