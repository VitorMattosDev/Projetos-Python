'''
Para este desafio, quero que você peça ao usuário que
digite um número. Se o núero for maior que 10, imprima
"O númeo é maior que 10". Caso contrário, imprima
"O número é menor ou igual a 10".
'''

num = int(input("Digite um número: "))  # Solicita ao usuário que digite um número e converte a entrada para inteiro

if num > 10:  # Verifica se o número é maior que 10
    print("O número é maior que 10")  # Imprime se a condição for verdadeira
else:
    print("O número é menor ou igual a 10")  # Imprime se a condição for falsa

# EXEMPLOS DE SAÍDA PARA ENTRADAS 15 E 8    :
# Digite um número: 15
# O número é maior que 10

# Digite um número: 8
# O número é menor ou igual a 10