'''
Para este desafio, crie uma função lambda que
aceite um número e retorne o cubo desse número.
'''

# Solução:
cubo = lambda x: x ** 3

numero = int(input("Digite um número: "))
resultado = cubo(numero)
print(f"O cubo de {numero} é {resultado}")
