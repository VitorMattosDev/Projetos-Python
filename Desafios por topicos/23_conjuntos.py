'''
Para este desafio, crie dois conjuntos, cada um contendo
5 nomes de seus amigos. Alguns nomes devem estar
presentes em ambos os conjuntos. Use um método para
encontrar quais nomes aparecem em ambos os conjuntos
e imprima o resultado.
'''

# Cria dois conjuntos com nomes de amigos
amigos_conjunto1 = {'Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'}
amigos_conjunto2 = {'Carlos', 'Diana', 'Fernanda', 'Gustavo', 'Helena'}

# Encontra os nomes em ambos os conjuntos
nomes_comuns = amigos_conjunto1.intersection(amigos_conjunto2)

# Outra forma de encontrar os nomes comuns usando o operador &
# nomes_comuns = amigos_conjunto1 & amigos_conjunto2

print(nomes_comuns)  # Exibe os nomes que aparecem em ambos os conjuntos