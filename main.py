import json
import os
import cadastro

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

def menu():
    while True:
        print(cor.VERDE + "---> Sistema cimentogames <---")
        print(cor.CIANO + "    1 - Modulo usuarios")
        print(cor.CIANO + "    2 - 2 crud")
        print(cor.CIANO + "    3 - 3 crud")
        print(cor.CIANO + "    0 - Sair")
    
        opcao = int(input(cor.VERDE + "escolha uma das opções acima: "))

        if(opcao == 1):
            cadastro.menu()
            continue
        elif(opcao == 2):
            print("aqui vai ficar o 2° crud")
            continue
        elif(opcao == 3):
            print("aqui vai ficar o 3° crud")
            continue
        else:
            print(cor.VERMELHO + "Saindo...")
            break
            
menu()