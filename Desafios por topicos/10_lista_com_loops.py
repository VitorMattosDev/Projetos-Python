'''
Para este desafio, comece com a lista 'frutas' do desafio anterior. Use um "for loop" para percorrer
a lista e imprima cada fruta precedida pelo texto "Eu gosto de ".
'''

frutas = ['maçã', 'morango', 'uva']  # Lista fornecida no desafio anterior

for fruta in frutas:  # Percorre cada fruta na lista 'frutas'. A variável 'fruta' representa o item atual na iteração. Por exemplo, na primeira iteração, 'fruta' será 'maçã', na segunda iteração, 'fruta' será 'morango', e assim por diante. Ou seja, Para {item atual} em {lista que deseja percorrer}
    print(f"Eu gosto de {fruta}")  # Imprime cada fruta precedida pelo texto "Eu gosto de "

# Saída esperada:
# Eu gosto de maçã
# Eu gosto de morango
# Eu gosto de uva


# Uma alternativa ao loop é usar o próprio print, embora seja muito repetitivo
# print("Eu gosto de", frutas[0])
# print("Eu gosto de", frutas[1])
# print("Eu gosto de", frutas[2])

# Caso a lista tenha 1000 itens, é inviável utilizar a alternativa acima. O loop for imprimiria todos os itens em apenas 2 linhas de código.