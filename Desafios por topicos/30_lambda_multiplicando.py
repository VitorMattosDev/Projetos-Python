'''
Para este desafio, crie uma função lambda
que aceite dois números e retorne a multiplicação
desses números.
'''

# Solução:
multiplicar = lambda x, y: x * y

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = multiplicar(numero1, numero2)
print(f"A multiplicação de {numero1} e {numero2} é {resultado}")