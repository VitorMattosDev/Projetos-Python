'''
Neste desafio, quero que você crie um script que solicite ao usuário dois números.
Em seguida, seu script deve imprimir a soma, a subtração, a multiplicação, a divisão (em decimal)
e a exponenciação (primeiro número elevado ao segundo número) desses dois números.
'''

# Solicita ao usuário que digite o primeiro número e converte para float
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que digite o segundo número e converte para float
num2 = float(input("Digite o segundo número: "))

print(num1 + num2)      # Soma dos dois números
print(num1 - num2)      # Subtração do segundo número do primeiro
print(num1 * num2)      # Multiplicação dos dois números
print(num1 / num2)      # Divisão do primeiro número pelo segundo (resultado decimal)
print(num1 ** num2)     # Exponenciação: primeiro número elevado