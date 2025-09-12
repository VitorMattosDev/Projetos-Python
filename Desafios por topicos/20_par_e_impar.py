'''
Para este desafio, crie uma lista de números de 1 a 10.
Use um 'for loop' para iterar sobre a lista. Se o número
atual da iteração for par, imprima "O número [número] é par".
Se o número for ímpar, imprima "O número [número] é ímpar".
'''

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Isso seria uma lista com os números de 1 a 10
numeros = list(range(1, 11)) # Usando range para criar a lista de números de 1 a 10

for numero in numeros:
    if numero % 2 == 0: # Verifica se o número é par
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")