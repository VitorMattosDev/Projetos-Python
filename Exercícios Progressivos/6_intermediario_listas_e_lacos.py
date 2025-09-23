numeros = input("Digite 5 numeros separados por espaco: ")

numeros = [int(x) for x in numeros.split(" ")]

ordenado = sorted(numeros)

print(ordenado)