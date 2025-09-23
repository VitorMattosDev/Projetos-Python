def media(numeros):
    return sum(numeros) / len(numeros)

numeros = input("Digite os numeros separados por espaco: ")

numeros = [int(x) for x in numeros.split(" ")]

print(media(numeros))