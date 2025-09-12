'''
Para este desafio, crie um loop que peça ao usuário para digitar
o nome de uma fruta. Se a fruta digitada não for 'abacate', o loop deve
continuar pedindo ao usuário para digitar o nome de uma fruta. Se a fruta for
'abacate', o loop deve terminar e uma mensagem de parabéns deve ser exibida.
'''

while True:
    fruta = input("Digite o nome de uma fruta: ")
    if fruta.lower() == 'abacate':
        break

print("Parabéns, você acertou a fruta!")