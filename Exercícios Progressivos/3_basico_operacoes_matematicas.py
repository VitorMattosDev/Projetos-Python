numeros = input("Digite dois numeros separados por espaco: ")

num1, num2 = numeros.split(" ")

print(f"Soma: {int(num1) + int(num2)}")
print(f"Subtracao: {int(num1) - int(num2)}")
print(f"Multiplicacao: {int(num1) * int(num2)}")
print(f"Divisao: {int(num1) / int(num2)}")