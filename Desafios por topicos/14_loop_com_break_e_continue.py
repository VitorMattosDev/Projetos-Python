'''
Para este desafio, quero que você crie um loop que imprima
os números de 1 a 10, mas pare de imprimir assim que chegar a 5
usando o comando 'break'. Em seguida, crie um segundo loop
que imprima os números de 1 a 10, mas pule a impressão do número 5 
usando o comando 'continue'.
'''

# O break e o continue são válidos para loops while e for. Vou utilizar ambos os loops como exemplo

# ======= UTILIZANDO O BREK COM LOOP WHILE =======

print("Inicio do loop WHILE")

num = 1

while num <= 10:
    if num == 5:
        break  # Interrompe o loop quando num é igual a 5
    print(num)  # Imprime o número atual
    num += 1  # Incrementa num em 1 para a próxima iteração do loop

print("Loop WHILE concluido")


# ======= UTILIZANDO O CONTINUE COM LOOP FOR =======
print("Inicio do loop FOR")


for num in range(1, 11):  # Gera números de 1 a 10
    if num == 5:
        continue  # Pula a iteração quando num é igual a 5
    print(num)  # Imprime o número atual

print("Loop FOR concluido")

# SAÍDA:
# Inicio do loop WHILE
# 1
# 2
# 3
# 4
# Loop WHILE concluido
# Inicio do loop FOR
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# Loop FOR concluido

# Nota-se que o loop while parou ao chegar no 5, enquanto o loop for pulou o 5 e continuou imprimindo os números seguintes. Isso porque o comando break interrompe o loop por completo, enquanto o comando continue apenas pula a iteração atual (5 -> 6) e continua com a próxima e por isso, pula do 4 para o 6 na saída.
