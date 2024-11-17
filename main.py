import json
import os
import cadastro
import perfil
import metas
import investimentos

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
        print("    3 - Modulo investimentos")
        print("    4 - Modulo metas")
        print("    0 - Sair")
    
        opcao = int(input("Escolha uma das opções acima: "))

        if(opcao == 1):
            cadastro.menu()
            continue
        elif(opcao == 2):
            perfil.menu()
            continue
        elif(opcao == 3):
            investimentos.menu()
            continue
        elif(opcao== 4):
            metas.menu()
            continue
        else:
            print("Saindo...")
            break
            
menu()
