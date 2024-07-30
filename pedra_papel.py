import random

print('Bem vindo, vamos jogar joken pô')



opcoes = ['pedra', 'papel', 'tesoura']
while True:
    us = str(input('Faça sua jogada: ')).lower()
    if us not in opcoes:
        print('Escreve direito bocó')

    pc = random.choice(opcoes)
    print('Jogada do PC: {}'.format(pc))
    
    if us == pc:
        print('Empate, tente novamente ')

    elif us == 'papel' and pc == 'pedra' or us == 'pedra' and pc == 'tesoura' or us == 'tesoura' and pc == 'papel':
        print('Parabens, você venceu!')
        break
    else:
        print('Perdeu, tente novamente')
    