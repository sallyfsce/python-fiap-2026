# EXERCÍCIOS DO PDF

'''
Calcule a área de um círculo com raio 5. Use a fórmula: área = π * raio^2.
(Dica: você pode usar 3.14159 como valor aproximado de π).
'''

raio = 5
pi = 3.1415
area = pi * raio**2
print("Qual é a área?")
print(f"A área é: {area}")

'''
Converta uma temperatura de Fahrenheit para Celsius. 
A fórmula de conversão é: Celsius = (Fahrenheit - 32) * 5/9
'''

# FAHRENHEIT ESCOLHIDO: 212

fahrenheit = 212
celsius = (fahrenheit - 32) * 5/9
print('Qual é a temperatura em celsius?')
print(f'A temperatura é: {celsius}')

'''
▪ Você comprou 3 livros por R$ 25 cada e 2 canetas por R$ 5 cada. Calcule o total gasto.
'''

livre = 25
canete = 5
totale_gaste = livre * 3 + canete * 2
print("Quale totale gaste?")
print(f'O totale gaste e:{totale_gaste}')

'''
Um carro percorreu 150 km a uma velocidade média de 60 km/h. Quanto tempo (em horas) o carro
levou para percorrer essa distância?
'''

carro = 150
velocidade = 60
tempo = carro / velocidade
print(f'O tempo gasto em horas: {tempo}')

'''
Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
aritmética do aluno.
'''

valor1 = 8
valor2 = 7
media = (valor1 + valor2) / 2
print(f'A média é: {media}')

#OU

nota1 = float(input("Digite a nota A: "))
nota2 = float(input("Digite a nota B: "))

media = nota1 + nota2 / 2

print(f'A média é: {media}')

'''
Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.
'''

nota3 = float(input("Digite a nota A: "))
nota4 = float(input("Digite a nota B: "))

media_ponderada = (nota3 * 4) + (nota4 * 6) / 10

print(f'A media ponderada do aluno é {media_ponderada}')

'''
Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que
o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor
unitário de cada peça2. Após, calcule e mostre o valor a ser pago.
'''

qtd1 = int(input('Quantidade de peças1: '))
valor_un1 = float(input('Valor da peça1:'))

qtd2 = int(input(f'Quantidade de peças2: '))
valor_un2 = float(input('Valor da peça2: '))

valor_peca2 = qtd2 * valor_un2
valor_peca1 = qtd1 * valor_un1
valort = valor_peca1 + valor_peca2
print(f'O valor total a ser pago é: {valort}')

'''
▪ Crie um programa que receba o valor do produto e valor pago.
▪ Calcule o troco a ser pago.
▪ O valor do troco deve ser exibido no terminal.
'''

valor_produto = float(input('Qual o valor do produto: R$ '))
valor_pago = float(input('Qual o valor pago: R$ '))

troco = valor_produto - valor_pago

if troco < 0:
    print('O valor é insuficiente para a compra')
else:
    print(f'O troco a ser devolvido é: {troco:.2f}')