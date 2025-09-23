def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
input = int(input("Digite um numero: "))
print(fatorial(input))