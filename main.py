import os
os.system('clear') 
from funcoes import *

# Jogo do chute, desenvolvido por Carlos Ribeiro
# O programa seleciona um número de 0 a 100 o 
# qual o usuário deverá tentar acertar.
# Quando encontrado o programa informa o
# número secreto e o numero de vezes que
# o usuário tentou até acertar.

print('''
    ********************** Jogo da Adivinhação **********************
      
    Tente adivinhar o número entre 0 e 100 sorteado pelo computador
    
    Para jogar digite 's + enter' para jogar ou 'n + enter' para sair:
''')

opcao = sim_ou_nao()
os.system('cls')
tentativas = []
while opcao == 's':
  print('Iniciando o jogo')
  print('Instruções:\nTente adivinhar o número entre 0 e 100 sorteado pelo computador:::')
  tentativas.append(chtutes())
  print(f'A média das suas tentativas até acertar foi {sum(tentativas)/len(tentativas)}')
  print(f'Segue a quantidade de tentativas nos últimos jogos {tentativas}')
  print('Deseja continuar jogando?')
  opcao = sim_ou_nao()
 
input('Programa finalizado, digite Enter qualquer tecla para sair.')