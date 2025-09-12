'''
Para este desafio, quero que você use a função range() em um "for loop" para imprimir os
números de 1 a 10 na tela.
'''

for numero in range(10):
    print(numero + 1)

# A função range(10) gera uma sequência de números de 0 a 9, Pois range(10) contabiliza 10 elementos começando do 0.
# Para começar do 1, podemos simplesmente adicionar +1 ao número impresso.

# Se quisermos que o range comece do 1 e vá até o 10, podemos usar range(1, 11)
# O primeiro número (1) é o início da sequência (inclusivo), e o segundo número (11) é o fim da sequência (exclusivo).
# Portanto, range(1, 11) gera números de 1 a 10.
# Usando range(1, 11):
# for numero in range(1, 11):
#     print(numero) # Isso imprimirá os números de 1 a 10 diretamente sem necessidade de adicionar +1, pois o range já começa do 1 e termina no 11 sem incluir o 11.

# ===================================================
# No exemplo utilizado:
# for numero in range(10):  # Percorre os números de 0 a 9
#     print(numero + 1)  # Imprime cada número incrementado em 1

# Na primeira iteração, 'numero' será 0, então 'numero + 1' será 1. Temos então: print(0 + 1) -> print(1)
# Na segunda iteração, 'numero' será 1, então 'numero + 1' será 2. Temos então: print(1 + 1) -> print(2)
# E assim por diante, até a última iteração onde 'numero' será 9, então 'numero + 1' será 10. Temos então: print(9 + 1) -> print(10)
# ===================================================