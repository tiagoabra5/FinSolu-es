import json
import os
import cadastro
import perfil

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
        print(f"---> {cor.AZUL}Sistema FinSoluções{cor.RESET} <---")
        print("    1 - Modulo usuarios")
        print("    2 - Modulo perfis")
        print("    3 - 3 crud")
        print("    0 - Sair")
    
        opcao = int(input("escolha uma das opções acima: "))

        if(opcao == 1):
            cadastro.menu()
            continue
        elif(opcao == 2):
            perfil.menu()
            continue
        elif(opcao == 3):
            print("aqui vai ficar o 3° crud")
            continue
        else:
            print("Saindo...")
            break
            
menu()
