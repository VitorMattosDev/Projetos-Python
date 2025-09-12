'''
Para este desafio, crie uma lista com os nomes de três cidades.
Peça ao usuário para digitar o nome de uma cidade.
Se a cidade estiver na lista, imprima "A cidade está na lista de cidades".
Se a cidade não estiver na tupla, imprima "A cidade não está na lista de cidades".

Obs: Você não pode utilizar list[]
'''

cidades = ('São Paulo', 'Rio de Janeiro', 'Belo Horizonte')  # Criando uma tupla com os nomes das cidades

cidade_desejada = input("Digite o nome de uma cidade: ")  # Solicitando ao usuário que digite o nome de uma cidade

if cidade_desejada in cidades:  # Verificando se a cidade digitada está na tupla
    print("A cidade esta na lista de cidades")  # Imprimindo se a cidade estiver na tupla
else:
    print("A cidade não está na lista de cidades")  # Imprimindo se a cidade não estiver na tupla