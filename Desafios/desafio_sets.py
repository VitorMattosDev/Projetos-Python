'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista 1 = Funcionários que tem carro e trabalham a noite
Lista 2 = Funcionários que tem carro e trabalham durante o dia
Lista 3 = Funcionários que não tem carro
'''
#TIPOS LIST

# funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
# turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
# turno_noite = ['Pedro', 'Sophia', 'Bruno']
# tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#====================================================================

#TIPOS SET

# funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
# turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
# turno_noite = {'Pedro', 'Sophia', 'Bruno'}
# tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

#====================================================================

#Solução com List Comprehension (FUNCIONA COM LIST E SET)


# lista1 = [i for i in funcionarios if i in tem_carro and i in turno_noite]
# lista2 = [i for i in funcionarios if i in tem_carro and i in turno_dia]
# lista3 = [i for i in funcionarios if i not in tem_carro]



#Solução com Sets (FUNCIONA SOMENTE COM SET POR CONTA DAS OPERAÇÕES DE CONJUNTOS & E -)

# lista1 = list(tem_carro & turno_noite)
# lista2 = list(tem_carro & turno_dia)
# lista3 = list(funcionarios - tem_carro)

print('Tem carro e trabalha a noite: ', lista1)
print('Tem carro e trabalha de dia: ', lista2)
print('Não tem carro: ', lista3)
