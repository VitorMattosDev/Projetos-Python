'''
Para este desafio, crie uma lista com 5 nomes de países e as capitais
desses países. Peça ao usuário para digitar o nome de um país. Se o país
estiver na lista, imprima "A capital de [país] é [capital]". Se o país
não estiver na lista, imprima "País não encontrado na lista".
'''

# Cria um dicionário com países como chave e capitais como valor
paises_e_capitais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Uruguay': 'Montevideo',
    'Chile': 'Santiago',
    'Paraguay': 'Asuncião'
}

# Solicita ao usuário que digite o nome de um país
pais_desejado = input("Digite o nome de um país: ")

# Verifica se o país está no dicionário de países e capitais
if pais_desejado in paises_e_capitais:
    capital = paises_e_capitais[pais_desejado]  # Obtém a capital do país informado
    print(f"A capital de {pais_desejado} é {capital}.")  # Exibe a capital do país
else:
    print("País não encontrado na lista.")  # Mensagem caso o país não esteja na lista