'''
Ex 1 faco depois
▪ Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
'''

'''
EXERCÍCIO 2
▪ Faça um programa que leia um número, e informe se ele é par ou impar
'''

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')

'''
EXERCÍCIO 3
▪ Faça um programa que peça dois números 
e imprima o maior deles, e informe caso eles sejam iguais
'''

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

if numero1 > numero2:
    print(f'{numero1}')
elif numero2 > numero1:
    print (f'{numero2}')
else:
    print('Os números são iguais')



'''
EXERCÍCIO 5
▪ Faça um programa que leia 2 valores inteiros (A e B).
▪ A seguir, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando
se os valores lidos são múltiplos entre si.
'''

num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira outro número inteiro: '))

if num1 % num2 == 0:
    print('São múltiplos')
else:
    print('Não são múltiplos')

'''
Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações
matemáticas (+, -, *, /)
▪ O programa deve calcular o valor final de acordo com a operação selecionada.
▪ Ou seja, se a entrada for 5, 6 e *, então seu programa dever mostrar 30
'''

numa = float(input('Insira um número'))
numb = float(input('Insira outro número'))
op = input('Insira o caractere da operação matemática desejada (+, -, *, /)')

if op == '+':
    print(f'{numa + numb}')

if op == '-':
    print(f'{numa - numb}')

if op == '*':
    print(f'{numa * numb}')

if op == '/':
    print(f'{numa / numb}')

'''
EXERCÍCIO 7
▪ Faça um programa que receba o ano de nascimento da pessoa e retorne:
▪ Se o voto é obrigatório este ano;
▪ Se o voto é opcional este ano;
▪ Se o voto é proibido este ano.
'''

idade = int(input('Insira sua idade: '))

if idade < 16:
    print('O voto é proibido este ano')

if idade == 16 < 18:
    print('O voto é opcional este ano')

if idade >= 18:
    print('O voto é obrigatório este ano')

    '''
EXERCÍCIO 8
▪ Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
no salário atual:
▪ Salários até R$ 280,00 (incluindo): aumento de 20%.
▪ Salários entre R$ 280,00 e R$ 700,00: aumento de 15%.
▪ Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%.
▪ Salários de R$ 1500,00 em diante: aumento de 5%.
▪ Após o aumento ser realizado, informe na tela:
▪ O salário antes do reajuste.
▪ O percentual de aumento aplicado.
▪ O valor do aumento.
▪ O novo salário, após o aumento
    '''

salario1 = float(input('Insira aqui o seu salário'))


if salario1 < 280:
    percentual = 20
elif salario1 >= 280 <= 700:
    percentual = 15
elif salario1 > 700 <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario1 * (percentual / 100)


print(f'Salário antes do reajuste: {salario1:.2f}')
print(f'Percentual de aumento: {percentual}')
print(f'Valor do aumento: {aumento}')
print(f'Salário após aumento: {salario1 + aumento}')

'''
EXERCÍCIO 9
▪ Faça um programa que recebe:
▪ o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
▪ o peso da carga do caminhão em toneladas
▪ o código da carga, supondo que é um número inteiro de 10 e 40
▪ Seu programa deve calcular:
▪ o peso da carga do caminhão convertido em quilos
▪ o preço da carga do caminhão
▪ valor do imposto que e cobrado com base no preço da carga e do estado de origem
▪ o valor total transportado pelo caminhão (carga + impostos)
'''

cod = int(input('Insira o número do estado de origem: '))
if cod < 1 or cod > 5:
    print('Esse não é um número válido.')

peso = float(input('Insira o peso do caminhão(em toneladas): '))

cod_carga = int(input('Insira o código da carga: '))
if cod_carga > 40 or cod_carga < 10:
    print('Esse não é um número válido.')

if cod == 1:
    imposto = 35
elif cod == 2:
    imposto = 25
elif cod == 3:
    imposto = 15
elif cod == 4:
    imposto = 5
else:
    imposto = 0

if 10 <= cod_carga <= 20:
    preco = 100
elif 21 <= cod_carga <= 30:
    preco = 250
elif 31 <= cod_carga <= 40:
    preco = 340


peso_kg = peso * 1000
preco_carga = peso_kg * preco
valor_imposto = preco_carga * (imposto / 100)
valor_total = valor_imposto + preco_carga
print(f'O peso em kg: {peso_kg:.2f} kg')
print (f'Preço da carga: R${preco_carga:.2f}')
print(f'Valor do imposto: R${valor_imposto:.2f}')
print(f'O valor total é de: R${valor_total:.2f}')

'''
EXERCÍCIO 10
▪ Faça um programa que leia 3 valores que representam os lados de um triângulo A, B e C e ordene-os
em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o
tipo de triângulo que estes três lados formam, com base nos seguintes casos:
▪ Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
▪ Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
▪ Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
▪ Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;
▪ Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
▪ Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;
'''
