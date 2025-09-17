'''
Para este desafio, crie uma função que aceite dois números como entrada
e retorne a soma desses números
'''

def somar_numeros(num1, num2):
    return num1 + num2  # Retorna a soma dos dois números

# Solicita ao usuário que digite dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chama a função para calcular a soma dos dois números
soma = somar_numeros(numero1, numero2)

# Imprime a soma dos dois números
print(f"A soma de {numero1} e {numero2} é {soma}")