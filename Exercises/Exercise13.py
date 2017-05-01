many = int(input("How many fibonacci numbers: "))

def fibonacci(number):
    lista = [1, 1]

    if number == 1:
        return lista[0]
    elif number == 2:
        return lista
    else:
        for i in range(1, number - 1):
            lista.append(lista[i - 1] + lista[i])
        return lista

l = fibonacci(many)

for i in range(len(l)):
    print(l[i])
