# Este programa solicita ao usuário a temperatura interna de uma carne em Celsius
# e informa o ponto de cozimento correspondente, de acordo com faixas de temperatura.

temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura < 48:
    print("Deixe cozinhar por mais tempo.")
elif temperatura < 54:
    print("A carne está selada.")
elif temperatura < 60:
    print("A carne está ao ponto para mal passada.")
elif temperatura < 65:
    print("A carne está ao ponto.")
elif temperatura < 71:
    print("A carne está ao ponto para bem passada.")
elif temperatura == 71:
    print("A carne está bem passada.")
elif temperatura > 71:
    print("A carne está queimada.")
else:
    print("Temperatura inválida.")