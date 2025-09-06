'''
Calculo de IMC - ÍNCICE DE MASSA CORPORAL

Qual é a altura em cm:
Qual é o peso em kg:


MENOR QUE 18,5 = MAGREZA
ENTRE 18,5 E 24,9 = NORMAL
ENTRE 25,0 E 29,9 = SOBREPESO
ENTRE 30,0 E 39,9 = OBESIDADE
MAIOR QUE 40,0 = OBESIDADE GRAVE
'''


def calcularIMC(peso, altura):
    imc = peso / (altura / 100) ** 2
    return imc

def classificarIMC(imc):
    if imc < 18.5:
        return 'MAGREZA'
    elif imc <= 24.9:
        return 'NORMAL'
    elif imc <= 29.9:
        return 'SOBREPESO'
    elif imc <= 39.9:
        return 'OBESIDADE'
    else:
        return 'OBESIDADE GRAVE'
    
def main():
    try:
        altura = float(input('Qual é a altura em cm: ')) 
        peso = float(input('Qual é o peso em kg: '))
        
        imc = calcularIMC(peso, altura)
        classificacao = classificarIMC(imc)
        
        print(f'Seu IMC é {imc:.2f} e sua classificação é {classificacao}.')

    except ValueError:
        print("Por favor, insira valores numéricos válidos para altura e peso.")

if __name__ == "__main__": # Evitar que o main seja executado automaticamente caso esse arquivo seja importado em outro programa
    main()# Executa todo o fluxo do programa do desafio_imc.py