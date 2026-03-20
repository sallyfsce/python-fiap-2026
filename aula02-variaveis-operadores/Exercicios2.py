# EXERCÍCIOS DE PYTHON PARA TREINAR

'''
Crie um programa que peça o nome do usuário e mostre:
Olá, [nome]!
'''

nome = input('Qual o seu nome? ')
print(f'Olá, {nome}!')

'''
Peça a idade do usuário e mostre:
A idade digitada
Quantos anos ele terá daqui a 10 anos.
'''

idade = int(input('Qual a sua idade? '))
print(f'Você tem {idade} anos')
soma = idade + 10
print(f'Daqui dez anos, terá {soma} anos')

'''
Peça dois números e mostre a soma deles.
'''

numero1 = int(input('Qual o primeiro numero? '))
numero2 = int(input('Qual o segundo numero? '))
soma = numero1 + numero2
print(f'A soma desses dois números é {soma}')

'''
Peça dois números e mostre:
Soma
Subtração
Multiplicação
Divisão
'''
numero1 = int(input('Qual o primeiro numero? '))
numero2 = int(input('Qual o segundo numero? '))
soma = numero1 + numero2
sub = numero1 - numero2
mul = numero1 * numero2
div = numero1 / numero2
print(f'Essas são as operações com os seus números, {soma}, {sub}, {mul}, {div} ')

'''
Peça um número e mostre:

O dobro
O triplo
A raiz quadrada
'''

numero = int(input('Qual o numero? '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f'{dobro}, {triplo}, {raiz}')

'''
Peça a idade de uma pessoa e diga se ela é:
Menor de idade
Maior de idade
'''

idade = int(input('Qual a sua idade? '))
if idade >= 18:
    print('Você é maior de idade!')
elif idade < 18:
    print('Você é menor de idade')

'''
Peça um número e diga se ele é:

Par
Ímpar
'''

numero = int(input('Qual o numero? '))
if numero % 2 == 0:
    print('Par')
else:
    print('Impar')

'''
Peça a nota de um aluno e mostre:

Aprovado (nota ≥ 7)
Recuperação (5 a 6)
Reprovado (< 5)
'''

nota = float(input('Qual a sua nota? '))
if nota >= 7:
    print('Aprovado')
elif 5 <= nota <= 6:
    print('Recuperação')
else:
    print('Reprovado')

'''
Peça o salário de uma pessoa e calcule um aumento de 10%.
'''

salario = float(input('Qual é seu salário'))
aumento = salario * 10 / 100
salario_aumento = salario + aumento
print(f'Seu aumento é de {aumento:.2f} e seu salário total é {salario_aumento:.2f}')

'''
Crie um programa que converta:

Reais → Dólares
(você pode usar um valor fixo, tipo 1 dólar = 5 reais)
'''

real = float(input('Quantos reais você quer converter? '))
dolar = 4
convertida = real / dolar
print(f'Isso converte em: {convertida:.2f} dolares')

'''
Peça a altura e o peso de uma pessoa e calcule o IMC.
'''

altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura * altura)
print(f'Seu imc é: {imc}')

'''
Mostre os números de 1 até 10 usando for.
'''