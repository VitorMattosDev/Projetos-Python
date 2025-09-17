'''
Crie uma função que aceita um número como entrada
e retorna o quadrado desse número.
'''

def calcular_quadrado(numero):
    return numero ** 2  # Retorna o quadrado do número

# Solicita ao usuário que digite um número
numero_usuario = float(input("Digite um número: "))

# Chama a função para calcular o quadrado do número
quadrado = calcular_quadrado(numero_usuario)

# Imprime o quadrado do número
print(f"O quadrado de {numero_usuario} é {quadrado}")