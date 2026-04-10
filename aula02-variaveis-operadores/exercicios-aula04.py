'''
EXERCÍCIO 1
▪ Faça um programa que exiba a mensagem “Olá, Mundo”.
▪ Essa mensagem deverá ser exibida repetidamente.
▪ Ao final de toda iteração da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem
novamente.
▪ Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”.
'''

while True:
    print('Olá, mundo!')

    resposta = input('Deseja exibir a mensagem novamente? (s/n): ')

    if resposta.lower() != 's':
        break

print('Fim')

'''
EXERCÍCIO 2
▪ Contagem de 0 a 100 pulando de 10 em 10.
▪ O terminal deve ficar assim:
0
10
20
30
40
50
60
70
80
90
100
'''

for i in range(0, 101, 10):
    print(i)

'''
Faça um programa que receba um número n
▪ Exiba a tabuada deste número do 0 ao 25.
▪ Utilize laços de repetição
'''