'''
Para este desafio, crie uma função que calcule a potência de um número.
A função deve aceitar dois argumentos: a base e o expoente. No entanto,
se o expoente não for fornecido, ele deve assumir o valor padrão de 2.
'''

def potencia(base, expoente=2):
    """Calcula a potência de um número com expoente padrão 2."""
    return base ** expoente

try:
    base = float(input("Digite a base: "))
    expoente_input = input("Digite o expoente (pressione Enter para usar o valor padrão 2): ").strip()

    # Usa o valor padrão se o usuário não digitar nada ou digitar apenas espaços
    if expoente_input:
        expoente = float(expoente_input)
        print(f"{base} elevado a {expoente} é {potencia(base, expoente)}")
    else:
        print(f"{base} elevado ao quadrado é {potencia(base)}")
except ValueError:
    print("Por favor, digite valores numéricos válidos para a base e o expoente.")