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
ex 4 ja fez
'''

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