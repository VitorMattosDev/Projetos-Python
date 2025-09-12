'''
Para este desafio, quero que você use um loop (não pode ser o for loop)
para imprimir os números de 1 a 10 na tela.
'''

numero = 1  # Inicializa a variável 'numero' com o valor 1

while numero <= 10:  # Enquanto 'numero' for menor ou igual a 10
    print(numero)  # Imprime o valor atual de 'numero'
    numero += 1  # Incrementa 'numero' em 1

# Explicação:
# 1. Inicializamos a variável 'numero' com o valor 1.
# 2. Usamos um loop 'while' que continua enquanto 'numero' for menor ou igual a 10.
# 3. Dentro do loop, imprimimos o valor atual de 'numero'.
# 4. Em seguida, incrementamos 'numero' em 1 para a proxima iteração do loop.

# O trecho numero += 1 é uma forma abreviada de escrever numero = numero + 1,
# que atualiza o valor de 'numero' somando 1 ao seu valor atual.
# Como a variável 'numero' começa em 1 e é incrementada em 1 a cada iteração,

#EXEMPLO DA PRIMEIRA ITERAÇÃO COM VALORES DEFINIDOS:
# numero = 1
# while 1 <= 10:  # Verdadeiro, então o loop continua
#     print(1)  # Imprime 1
#     numero += 1  # Agora numero é 2, pois numero = numero(que é 1) + 1 = (1+1 = 2)

# o loop continuará até que 'numero' atinja 11, momento em que a condição while será falsa