import json
import os
from time import sleep

arquivo = "perfil.json"

def carregar_usuarios():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

def criar_perfil_usuario(nome, renda_mensal, vm_despesas_mensais, div_pendentes, vm_div_pendentes, objetivos, vm_entretenimento, vm_educ_saude, formas_pagamento):
    usuarios = carregar_usuarios()

    novo_usuario = {
        "nome": nome,
        "renda mensal": renda_mensal,
        "valor das despesas": vm_despesas_mensais,
        "dividas pendentes": div_pendentes,
        "valor das dívidas": vm_div_pendentes,
        "objetivos financeiros": objetivos,
        "gasto com entretenimento": vm_entretenimento,
        "gasto com saúde e educação": vm_educ_saude,
        "formas de pagamento comum": formas_pagamento,
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    sleep (1)
    print("USUÁRIO ADICIONADO COM SUCESSO!")

def listar_usuarios():
    usuarios = carregar_usuarios()

    if usuarios:
        print("LISTA DE USUÁRIOS:")
        for usuario in usuarios:
            print("-" * 50)
            for chave, valor in usuario.items():
                print(f"{chave.upper()}: {valor}")
            print("-" * 50)
    else:
        sleep (1)
        print("NENHUM USUÁRIO CADASTRADO.")

def atualizar_usuario(nome_antigo, novo_nome, nova_renda, nova_despesa, nova_causa_divida, novo_vm_divida, novo_objetivo, novo_vm_entretenimento, novo_vm_educ_saude, nova_fpagamento):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario['nome'] == nome_antigo:
            usuario['nome'] = novo_nome
            usuario['renda mensal'] = nova_renda
            usuario['valor das despesas'] = nova_despesa
            usuario['dividas pendentes'] = nova_causa_divida
            usuario['valor das dívidas'] = novo_vm_divida
            usuario['objetivos financeiros'] = novo_objetivo
            usuario['gasto com entretenimento'] = novo_vm_entretenimento
            usuario['gasto com saúde e educação'] = novo_vm_educ_saude
            usuario['formas de pagamento comum'] = nova_fpagamento
            break
    salvar_usuarios(usuarios)
    sleep (1)
    print("USUÁRIO ATUALIZADO COM SUCESSO!")

def excluir_usuario(nome):
    usuarios = carregar_usuarios()
    usuarios = [usuario for usuario in usuarios if usuario['nome'] != nome]

    salvar_usuarios(usuarios)
    print("USUÁRIO EXCLUÍDO COM SUCESSO!")
    
def menu():
    while True:
        print("\nMENU PERFIL FINANCEIRO:")
        print("1 - Criar perfil de usuário")
        print("2 - Listar perfis")
        print("3 - Atualizar perfis")
        print("4 - Excluir perfis")
        print("0 - Voltar ao menu anterior")
        
        opcao = input("Escolha uma opção:\n>>> ")

        if opcao == "1":
            sleep(1)
            nome = input("Digite o nome:\n>>> ")
            renda_mensal = input("Digite a renda mensal:\n>>> ")
            vm_despesas_mensais = input("Digite o valor médio das despesas mensais:\n>>> ")
            div_pendentes = input("Digite as principais causas de dívidas:\n>>> ")
            vm_div_pendentes = input("Digite o valor médio dessas dívidas:\n>>> ")
            objetivos = input("Digite os objetivos financeiros:\n>>> ")
            vm_entretenimento = input("Digite os gastos com entretenimento:\n>>> ")
            vm_educ_saude = input("Digite os gastos com educação e saúde:\n>>> ")
            formas_pagamento = input("Digite as principais formas de pagamento:\n>>> ")
            criar_perfil_usuario(nome, renda_mensal, vm_despesas_mensais, div_pendentes, vm_div_pendentes, objetivos, vm_entretenimento, vm_educ_saude, formas_pagamento)
        elif opcao == "2":
            sleep(1)
            listar_usuarios()
        elif opcao == "3":
            sleep(1)
            nome_antigo = input("Digite o nome do usuário a ser atualizado:\n>>> ")
            novo_nome = input("Digite o novo nome:\n>>> ")
            nova_renda = input("Digite a nova renda mensal:\n>>> ")
            nova_despesa = input("Digite as novas despesas mensais:\n>>> ")
            nova_causa_divida = input("Digite a novas causas das dívidas:\n>>> ")
            novo_vm_divida = input("Digite o novo valor das dívidas:\n>>> ")
            novo_objetivo= input("Digite o novo objetivo:\n>>> ")
            novo_vm_entretenimento = input("Digite o novo valor gasto com entretenimento:\n>>> ")          
            novo_vm_educ_saude = input("Digite o novo valor gasto com educação e saúde:\n>>> ")         
            nova_fpagamento = input("Digite a nova forma de pagamento:\n>>> ")
                    
            atualizar_usuario(nome_antigo, novo_nome, nova_renda, nova_despesa, nova_causa_divida, novo_vm_divida, novo_objetivo, novo_vm_entretenimento, novo_vm_educ_saude, nova_fpagamento)
        elif opcao == "4":
            nome = input("Digite o nome do usuário a ser excluído:\n>>> ")
            sleep(1)
            excluir_usuario(nome)
        elif opcao == "0":
            print("Voltando ao menu anterior...")
            sleep(1)
            break
        else:
            print("Opção inválida. Tente novamente.")