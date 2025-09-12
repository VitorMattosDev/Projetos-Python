'''
Para este desafio, peça ao usuário para digitar a sua idade. Se a idade for
menos que 13, imprima "Você é uma criança". Se a idade estiver entre
13 e 19, imprima "Você é um adolescente". Se a idade for 20 ou mais,
imprima "Você é um adulto".
'''

idade = int(input("Digite sua idade: "))  # Solicita ao usuário que digite sua idade e converte para inteiro

if idade < 13:  # Verifica se a idade é menor que 13
    print("Voce é uma criança")  # Imprime se a condição for verdadeira
elif idade < 20:  # Verifica se a idade é menor que 20
    print("Voce é um adolescente")  # Imprime se a condição for verdadeira
else:  # Caso nenhuma condição seja verdadeira
    print("Voce é um adulto")  # Imprime se nenhuma condição for verdadeira

# EXPLICAÇÃO:
# 1. A função input() é usada para obter a idade do usuário.
# 2. A condição if verifica se a idade é menor que 13.
# 3. Se a condição for verdadeira, imprime "Voce é uma criança".
# 4. A condição elif verifica se a idade é menor que 20.
# 5. Se a condição for verdadeira, imprime "Voce é um adolescente".
# 6. Caso nenhuma condição seja verdadeira, imprime "Voce é um adulto".