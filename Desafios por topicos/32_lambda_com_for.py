'''
Para este desafio, crie uma função lambda que eleve um número ao
quadrado. Em seguida, use essa função para calcular o quadrado de 
todos os números em uma lista usando um loop for.
'''

# Solução:
quadrado = lambda x: x ** 2

lista_numeros = [1, 2, 3, 4, 5]

for numero in lista_numeros:
    quadrado_numero = quadrado(numero)
    print(f"O quadrado de {numero} é {quadrado_numero}")