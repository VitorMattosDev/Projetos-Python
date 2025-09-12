'''
Neste desafio, quero que você crie um script que pergunte o nome e a idade do usuário,
usando a função input(). Depois disso, o script deve imprimir uma mensagem que diga
"Olá, [nome]! Você tem [idade] anos.", substituindo [nome] e [idade] pelos valores
fornecidos pelo usuário.
'''

# Solicita ao usuário que digite seu nome e armazena o valor na variável 'nome'
nome = input("Qual é o seu nome? ")

# Solicita ao usuário que digite sua idade e armazena o valor na variável 'idade'
idade = input("Quantos anos você tem? ")

# Exibe uma mensagem personalizada usando os valores fornecidos pelo usuário
print(f"Olá, {nome}! Você tem {idade} anos.")