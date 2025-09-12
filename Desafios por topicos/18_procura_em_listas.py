'''
Para este desafio, imagine que você tem uma loja de carros. Crie uma
lista com os carros que você tem em estoque: BMW X6, BMW i5, BMW i8.
Peça ao usuário para que ele insira o nome do carro que deseja comprar.
Se o carro estiver em estoque, imprima "Este carro está disponível".
Se o carro não estiver em estoque, imprima "Desculpe, este carro não está
disponível".
'''
carros_em_estoque = ["BMW X6", "BMW i5", "BMW i8"]  # Lista de carros em estoque

# Solicita ao usuário que digite o nome do carro desejado e converte para minúsculas
carro_desejado = input("Digite o nome do carro que deseja comprar: ").lower()

# Verifica se o carro desejado está na lista de carros em estoque (ignorando maiúsculas/minúsculas)
if carro_desejado in [carro.lower() for carro in carros_em_estoque]:
    print("Este carro está disponível")  # Imprime se o carro estiver em estoque
else:
    print("Desculpe, este carro não está disponível")  # Imprime se o carro não estiver em estoque