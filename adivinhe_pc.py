"""
3 - Faça um programa que receba um número aleatório entre 1 e 11 e o computador deverá adivinhar qual número foi gerado.

- Solicite o nome do usuário.

- Solicite um número entre 1 e 11.

- O computador deverá gerar um palpite e informá-lo ao usuário.

- Caso o palpite esteja correto, finalize o programa. Caso esteja errado, pergunte se o valor é menor ou maior que o palpite do computador e gere um novo número de acordo.
"""
import random

valor = 0
randomico = random.randint(1, 11)
lista = []

print('Você vai jogar contra o computador. Digite abaixo um numero de 1 a 11. O computador não saberá qual numero você escolheu.')
jogador = int(input('Seu número: '))
print('Olá, sou o computador! É bom jogar com você!')
print(f'Meu Palpite é {randomico}, está correto?')
resposta = input('sim ou não?').upper()

while jogador != randomico:
    if resposta == 'sim'.upper():
        print('Você Ganhou!')
        print(lista)
    else:
        print('É maior ou menor?')
        x = input().upper()
        if x == 'maior'.upper():
            randomico = random.randint(jogador, 11)
            lista.append(randomico)
            if randomico != lista[::]:
                print(f'Meu Palpite é {randomico}, está correto?')
                resposta = input('sim ou não?').upper()
        elif x == 'menor'.upper():
            randomico = random.randint(1, jogador)
            lista.append(randomico)
            if randomico != lista[::]:
                print(f'Meu Palpite é {randomico}, está correto?')
                resposta = input('sim ou não?').upper()

print('Acertei!')
