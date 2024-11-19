import json
import os
from cadastro import *
from perfil import *
from investimentos import *
from metas import *

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
            menu_cadastro()
            continue
        elif(opcao == 2):
            menu_perfil()
            continue
        elif(opcao == 3):
            menu_investimentos()
            continue
        elif(opcao== 4):
            menu_metas()
            continue
        else:
            print("Saindo...")
            break
            
menu()
