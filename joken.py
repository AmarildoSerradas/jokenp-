import random

sinais = {
    'PEDRA': """
    _______
---'   ____)
      (_____)
      (_____)  PEDRA
      (____)
---.__(___)
""",
    'PAPEL': """
     _______
---'    ____)____
           ______)
          _______) PAPEL
         _______)
---.__________)
""",
    'TESOURA': """
    _______
---'   ____)____
          ______)
       __________) TESOURA
      (____)
---.__(___)
"""
}

robo = random.choice(list(sinais.keys()))






while True:
    print('''
    --------------------
    OLA BEM VINDO AO NOSSO JOGO DE PEDRA PAPEL E TESOURA
    DESEJA PARTICIPAR? ESCOLHA ENTRE SIM OU NÃO
    --------------------
''')
    joken = str(input("digite aqui: "))

    if joken.upper() == "SIM":
        print('''
        -----------
        BEM VINDO AO JOGO
        ESCOLHA ENTRE ELES:
        -----------
        ''')
        escolha = print('''
     1)     _______
        ---'   ____)
              (_____)
              (_____)   PEDRA
              (____)
        ---.__(___)


     2)   _______
     ---'    ____)____
               ______)
              _______)   PAPEL
             _______)
     ---.__________)

     3)  _______
     ---'   ____)____
              ______)
           __________) TESOURA
          (____)
     ---.__(___)


        --------------------
        Lembrando que
        Pedra > Tesoura
        Papel > Pedra
        Tesoura > Papel
        --------------------
        ''')

        humano = input('escolha entre as alternativas (PEDRA, PAPEL, TESOURA):')
        humano = humano.upper()

        if robo == 'PEDRA':

            if humano == 'PEDRA':
                 print('Parabens vocês empataram')
                 print('-'*20)
                 print(f'Seu sinal escolhido foi: {humano}')
                 print(sinais[humano])
                 print('-'*20)
                 print(f"O sinal escolhido pelo bot foi: {robo}")
                 print(sinais[robo])
                 input()

            elif humano == 'PAPEL':
                 
                 print('Parabens ! Usuario ganhou.')
                 print('-'*20)
                 print(f'Seu sinal escolhido foi: {humano}')
                 print(sinais[humano])
                 print('-'*20)
                 print(f"O sinal escolhido pelo bot foi: {robo}")
                 print(sinais[robo])
                 input()
            
            elif humano == 'TESOURA':

                print('Você perdeu!!! infelizmente o robo ganhou')
                print('-'*20)
                print(f'Seu sinal escolhido foi: {humano}')
                print(sinais[humano])
                print('-'*20)
                print(f"O sinal escolhido pelo bot foi: {robo}")
                print(sinais[robo])
                input()

        elif robo == 'PAPEL':

            if humano == 'PAPEL':
                 
                 print('Parabens vocês empataram')
                 print('-'*20)
                 print(f'Seu sinal escolhido foi: {humano}')
                 print(sinais[humano])
                 print('-'*20)
                 print(f"O sinal escolhido pelo bot foi: {robo}")
                 print(sinais[robo])
                 input()

            elif humano == 'TESOURA':
                 
                 print('Parabens ! Usuario ganhou.')
                 print('-'*20)
                 print(f'Seu sinal escolhido foi: {humano}')
                 print(sinais[humano])
                 print('-'*20)
                 print(f"O sinal escolhido pelo bot foi: {robo}")
                 print(sinais[robo])
                 input()

            elif humano == 'PEDRA':
                 print('Você perdeu!!! infelizmente o robo ganhou')
                 print('-'*20)
                 print(f'Seu sinal escolhido foi: {humano}')
                 print(sinais[humano])
                 print('-'*20)
                 print(f"O sinal escolhido pelo bot foi: {robo}")
                 print(sinais[robo])
                 input()

        elif robo == 'TESOURA':
            if humano == 'TESOURA':
                 print('Parabens vocês empataram')
                 print('-'*20)
                 print(f'Seu sinal escolhido foi: {humano}')
                 print(sinais[humano])
                 print('-'*20)
                 print(f"O sinal escolhido pelo bot foi: {robo}")
                 print(sinais[robo])
                 input()

            elif humano == 'PEDRA':
                 print('Parabens ! Usuario ganhou.')
                 print('-'*20)
                 print(f'Seu sinal escolhido foi: {humano}')
                 print(sinais[humano])
                 print('-'*20)
                 print(f"O sinal escolhido pelo bot foi: {robo}")
                 print(sinais[robo])
                 input()

            elif humano == 'PAPEL':
                print('Você perdeu!!! infelizmente o robo ganhou')
                print('-'*20)
                print(f'Seu sinal escolhido foi: {humano}')
                print(sinais[humano])
                print('-'*20)
                print(f"O sinal escolhido pelo bot foi: {robo}")
                print(sinais[robo])
                input()
        elif humano not in sinais:
            print(f'Seu sinal Não esta na lista\nTenta denovo.')

    elif joken.upper() == 'NÃO':

        print('OK, escolha sua. \n fechando programa!')
        break

    else:
        print('ESCOLHA ENTRE SIM OU NÃO')
