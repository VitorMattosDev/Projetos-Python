'''
Para este desafio, crie duas funções. A primeira função deve
aceitar um número e retornar o dobro desse número. A segunda
função deve aceitar um número e retornar o quadrado desse número.
Em seguida, chame a primeira função dentro da segunda para retornar o 
quadrado do dobro de um número.
'''

def dobrar_numero(numero):
    return numero * 2

def quadrado_numero(numero):
    return numero ** 2

numero = int(input("Digite um número: "))

quadrado_dobro = quadrado_numero(dobrar_numero(numero))
print(quadrado_dobro)