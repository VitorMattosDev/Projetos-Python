'''
Para este desafio, quero que você use a lista 'frutas' do desafio anterior. Seu desafio é
imprimir o primeiro e o último elemento da lista.
'''

frutas = ["maçã", "banana", "manga", "uva"]  # Lista fornecida no desafio anterior

print(frutas[0])  # Imprime o primeiro elemento da lista. frutas[0] é "maçã", frutas[1] é "banana", frutas[2] é "manga" e frutas[3] é "uva"
print(frutas[-1])  # Imprime o último elemento da lista. Índices negativos começam do fim da lista. frutas[-1] é "uva", frutas[-2] é "manga", frutas[-3] é "banana" e frutas[-4] é "maçã"

# Alternativamente, você também pode usar:
# print(frutas[len(frutas) - 1])  # Imprime o último elemento da lista, pois é o mesmo que frutas[4 - 1], pois o len(frutas) retorna o tamanho da lista (4 elementos). Subtraímos 1, pois os índices começão do zero, ou seja: 0 - Maçã, 1 - Banana, 2 - Manga, 3 - Uva

# Quando o tamanho da lista é conhecido, pode usar o índice direto, ou seja, frutas[3] para o último elemento "uva"
