'''
Para este desafio, comece com a lista 'frutas' do desafio anterior. Primeiro, seu desafio é
alterar o segundo elemento da lista (índice 1) de 'banana' para 'morango'. Depois disso, adicione a fruta
'abacaxi' ao final da lista. Por fim, imprima a lista modificada na tela.
'''

frutas = ["maçã", "banana", "manga", "uva"]  # Lista fornecida no desafio anterior

frutas[1] = "morango"  # Altera o segundo elemento da lista (índice 1) de 'banana' para 'morango'
frutas.append("abacaxi")  # Adiciona a fruta 'abacaxi' ao final da lista. A função append() adiciona um novo elemento ao final da lista

print(frutas)  # Imprime a lista modificada ['maçã', 'morango', 'manga', 'uva', 'abacaxi']