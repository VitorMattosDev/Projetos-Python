'''
Para este desafio, crie um lista de frutas e outra de
vegetais. Use um "for loop" aninhado (Nested for loop)
para imprimir todas as combinações possíveis de fruta e vegetais, com a
fruta primeiro e o vegetal em segundo.
'''

frutas = ["maçã", "banana", "manga"]  # Lista de frutas
vegetais = ["cenoura", "alface", "tomate"]  # Lista de vegetais

for fruta in frutas: # Loop externo para percorrer cada fruta na lista de frutas
    for vegetal in vegetais: # Loop interno para percorrer cada vegetal na lista de vegetais
        print(f"{fruta} e {vegetal}")

# Explicação:
# O primeiro loop "for fruta in frutas:" percorre cada fruta na lista de frutas.
# O segundo loop "for vegetal in vegetais:" percorre cada vegetal na lista de vegetais.
# Dentro de cada iteração do primeiro loop, o segundo loop imprime a combinação de fruta e vegetal.
# Ou seja, na primeira iteração do primeiro loop, 'fruta' será 'maçã', e o segundo loop imprimirá:
# maçã e cenoura
# maçã e alface
# maçã e tomate
# Na segunda iteração do primeiro loop, 'fruta' será 'banana', e o segundo loop imprimirá:
# banana e cenoura
# banana e alface
# banana e tomate
# E assim por diante, até que todas as combinações possíveis sejam impressas.