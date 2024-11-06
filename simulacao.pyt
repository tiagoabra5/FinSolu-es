import json
import os


arquivo_usuarios = os.path.join(os.path.dirname(__file__), 'usuarios.json')
arquivo_investimentos = os.path.join(os.path.dirname(__file__), 'investimentos.json')

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def adicionar_investimento(usuario, tipo_investimento, valor, prazo):
    investimentos = carregar_dados(arquivo_investimentos)
    novo_investimento = {
        'usuario': usuario,
        'tipo': tipo_investimento,
        'valor': valor,
        'prazo': prazo
    }
    investimentos.append(novo_investimento)
    salvar_dados(arquivo_investimentos, investimentos)
    print("✅ Investimento adicionado com sucesso!")

def calcular_montante_final(valor, prazo, tipo):

    taxa_juros = 0.005 if tipo == "Tesouro Direto" else 0.006
    montante_final = valor * (1 + taxa_juros) ** prazo
    return montante_final

def listar_investimentos(usuario):
    investimentos = carregar_dados(arquivo_investimentos)
    investimentos_usuario = [inv for inv in investimentos if inv.get('usuario') == usuario]
    if not investimentos_usuario:
        print("⚠ Nenhum investimento encontrado para este usuário.")
        return []

    print(f"\n{cor.VERDE}Investimentos para {usuario}:{cor.RESET}")
    for index, investimento in enumerate(investimentos_usuario):
        tipo = investimento.get('tipo')
        valor = investimento.get('valor', 0)
        prazo = investimento.get('prazo', 0)
        montante_final = calcular_montante_final(valor, prazo, tipo)
        print(f"ID: {index}")  
        print(f"   Tipo: {tipo}")
        print(f"   Valor inicial: R${valor:.2f}")
        print(f"   Prazo: {prazo} meses")
        print(f"   Montante final (simulado): R${montante_final:.2f}")
        print()

    return investimentos_usuario

def atualizar_investimento(usuario):
    investimentos_usuario = listar_investimentos(usuario)
    if not investimentos_usuario:
        return  

    escolha_id = int(input("Digite o ID do investimento que deseja atualizar: "))
    
    if escolha_id < 0 or escolha_id >= len(investimentos_usuario):
        print("⚠ ID de investimento inválido.")
        return

    investimento_selecionado = investimentos_usuario[escolha_id]
    novo_tipo = input("Novo tipo de investimento [1] Tesouro Direto ou [2] CDB : ")
    novo_valor = float(input("Novo valor: "))
    novo_prazo = int(input("Novo prazo (em meses): "))

  
    investimentos = carregar_dados(arquivo_investimentos)
    investimentos_totais = [
        inv if inv != investimento_selecionado else {
            'usuario': usuario,
            'tipo': novo_tipo,
            'valor': novo_valor,
            'prazo': novo_prazo
        } for inv in investimentos
    ]
    salvar_dados(arquivo_investimentos, investimentos_totais)
    print("✅ Investimento atualizado com sucesso!")

def excluir_investimento(usuario):
    investimentos_usuario = listar_investimentos(usuario)
    if not investimentos_usuario:
        return 

    escolha_id = int(input("Digite o ID do investimento que deseja excluir: "))
    
    if escolha_id < 0 or escolha_id >= len(investimentos_usuario):
        print("⚠ ID de investimento inválido.")
        return

    
    investimento_selecionado = investimentos_usuario[escolha_id]
    investimentos = carregar_dados(arquivo_investimentos)
    investimentos_totais = [inv for inv in investimentos if inv != investimento_selecionado]
    salvar_dados(arquivo_investimentos, investimentos_totais)
    print("✅ Investimento excluído com sucesso!")


def menu_investimentos():
    while True:
        print("\nMÓDULO DE INVESTIMENTOS:")
        print("1. Adicionar investimento")
        print("2. Listar investimentos")
        print("3. Atualizar investimento")
        print("4. Excluir investimento")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = input("Digite o nome do usuário: ")
            tipo_investimento = input("Tipo de investimento ([1] Tesouro Direto ou [2] CDB): ")
            valor = float(input("Valor do investimento: "))
            prazo = int(input("Prazo (em meses): "))
            adicionar_investimento(usuario, tipo_investimento, valor, prazo)
        elif opcao == "2":
            usuario = input("Digite o nome do usuário para listar os investimentos: ")
            listar_investimentos(usuario)
        elif opcao == "3":
            usuario = input("Digite o nome do usuário: ")
            atualizar_investimento(usuario)
        elif opcao == "4":
            usuario = input("Digite o nome do usuário: ")
            excluir_investimento(usuario)
        elif opcao == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("⚠ Opção inválida. Tente novamente.")