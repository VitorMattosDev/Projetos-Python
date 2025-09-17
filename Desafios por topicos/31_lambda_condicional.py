'''
Para este desafio, crie uma fução lambda que aceite um
número e retorne "´Par" se o número for par e "Ímpar" se
o número for ímpar.
'''

# Solução:
par_impar = lambda x: "Par" if x % 2 == 0 else "Ímpar"

numero = int(input("Digite um número: "))
resultado = par_impar(numero)

print(f"O número {numero} é {resultado}")