'''
Para este desafio, comece com a lista 'frutas' do desafio anterior. Primeiro remova a 'manga' da lista
usando o método remove(). Depois disso, remova o último item da lista usando o comando del. Por fim,
imprima a lista modificada na tela.
'''

frutas = ["maçã", "morango", "manga", "uva", "abacaxi"]  # Lista fornecida no desafio anterior

frutas.remove("manga")  # Remove a 'manga' da lista usando o método remove()
del frutas[-1]  # Remove o último item da lista usando o comando del

print(frutas)  # Imprime a lista modificada ['maçã', 'banana']