'''
Para este desafio, crie uma lista de frutas que inclui "maçã"
três vezes e outras frutas de sua escolha. Use um loop for para
contar quantas vezes "maçã" aparece na lista e imprima o resultado.
'''

frutas = ["maçã", "banana", "manga", "uva", "maçã", "laranja", "maçã"]  # Lista de frutas com "maçã" repetidas

contador = 0  # Inicializa o contador para contar as ocorrências de "maçã"

for fruta in frutas:  # Loop através de cada fruta na lista
    if fruta == "maçã":  # Verifica se a fruta atual é "maçã"
        contador += 1  # Incrementa o contador se for "maçã"

print(f"A palavra 'maçã' aparece {contador} vezes na lista.")  # Imprime o resultado

# SAÍDA:
# A palavra 'maçã' aparece 3 vezes na lista.