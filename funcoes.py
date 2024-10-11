import random
import os

# Gera inteiro aleatório
def gerar_numero():

    numero = random.randint(0,100)
    return numero


# Garante que o usuário digite s ou n
def sim_ou_nao():

    s_ou_n = False

    while not s_ou_n:

        resposta = str(input('Digite (s/n): '))

        if (resposta == 's' ) or (resposta == 'n' ):
            s_ou_n = True

        else:
            print('O valor digitado não é s/n!')
            s_ou_n = False

    return resposta



# Assegura que o número digitado pelo usuário é inteiro


def eh_numero():

    letra = True

    # Força o usuário a digitar inteiro, enquanto for um caractere 
    while letra:
        
        try:

            numero = int(input('Digite um número inteiro: '))
            letra = False

        except ValueError:

            print("O valor informado não é um inteiro!")
            letra = True
    
    return numero


def chtutes():

    # gera o número aleatório
    numero_secreto = gerar_numero()
    # pega o primeiro chute do usuário
    chute_do_usuario = eh_numero()
    tentativas = 1
    
    while (chute_do_usuario != numero_secreto):
    

        if (chute_do_usuario > numero_secreto):

            print('O número fornecido não é o número secreto! Você digitou um número maior que o número secreto.')
            chute_do_usuario = eh_numero()
            tentativas += 1
        
        else:

            print('O número digitado não é o número secreto! Você digitou um número menor que o número secreto.')
            chute_do_usuario = eh_numero()
            tentativas += 1
            
    print(f'Você acertou o número secreto {numero_secreto} depois de {tentativas} tentativas.')

    return tentativas

    