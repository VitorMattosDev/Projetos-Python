'''
As funções recursivas são funções que se chamam dentro
do seu próprio bloco de código. Elas são úteis para
resolver problemas que podem ser divididos em problemas menores
de natureza semelhante.

Um exemplo clássico de onde a recursão é usada é o cálculo do fatorial
de um número. O fatorial de um número n é o produto de todos os
números inteiro positivos de n até 1.
'''

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")