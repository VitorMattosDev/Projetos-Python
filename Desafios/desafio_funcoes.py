import math

'''
Programa que calcula a quantidade de latas de tinta necessárias para pintar uma parede.
O usuário informa o rendimento da tinta (m²/litro), altura e largura da parede (em metros).
O programa exibe a quantidade de latas necessárias.
'''

def calcular_quantidade_tinta(rendimento, altura, largura):
    area_parede = altura * largura
    qtd_latas = area_parede / rendimento
    return math.ceil(qtd_latas)

def obter_informacoes():
    try:
        dados = input("Informe o rendimento da tinta (m²/litro), altura (m) e largura (m) da parede, separados por espaço: ").split()
        rendimento = float(dados[0])
        altura = float(dados[1])
        largura = float(dados[2])
        if rendimento <= 0 or altura <= 0 or largura <= 0:
            raise ValueError # Força o bloco except a ser executado com exceção de ValueError
        return rendimento, altura, largura
    except (ValueError, IndexError):
        print("Entrada inválida. Por favor, insira números positivos separados por espaço.")
        return None

info = obter_informacoes()
if info:
    rendimento, altura, largura = info
    qtd_latas = calcular_quantidade_tinta(rendimento, altura, largura)
    print(f"Quantidade de latas de tinta necessárias: {qtd_latas}")


