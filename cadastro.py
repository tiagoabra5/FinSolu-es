import json
import os

arquivo = "usuarios.json"

def carregar_usuarios():
    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r") as infile:
                return json.load(infile)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return []
    return []

def salvar_usuarios(usuarios):
    with open(arquivo, 'w') as file:
        json.dump(usuarios, file, indent=4)   
        
def criar_usuarios(username, cpf, idade, genero, email, password, renda_mensal, fontes_renda_principais, categorias_despesas, despesas_mensais, valor_medio_despesas_mensais, dividas_pendentes, valor_medio_dividas_pendentes, capacidade_poupanca, objetivos_curto_prazo, objetivos_medio_prazo, objetivos_longo_prazo, gastos_entretenimento, valor_medio_entretenimento, padrao_consumo_servicos, valor_medio_pcs, gastos_educ_saude, valor_medio_educ_saude, principais_cartoes, forma_pagamento_comum):
    usuarios = carregar_usuarios()
    
    if cpf in usuarios:
        return "Usuario ja existe!"
    
    novo_usuario = {
        "username": username,
        "cpf": cpf,
        "idade": idade,
        "genero": genero,
        "email": email,
        "password": password,
        "renda_mensal": renda_mensal,
        "fontes_renda_principais": fontes_renda_principais,
        "categorias_despesas": categorias_despesas,
        "despesas_mensais": despesas_mensais,
        "valor_medio_despesas_mensais": valor_medio_despesas_mensais,
        "dividas_pendentes": dividas_pendentes,
        "valor_medio_dividas_pendentes": valor_medio_dividas_pendentes,
        "capacidade_poupanca": capacidade_poupanca,
        "objetivos_curto_prazo": objetivos_curto_prazo,
        "objetivos_medio_prazo": objetivos_medio_prazo,
        "objetivos_longo_prazo": objetivos_longo_prazo,
        "gastos_entretenimento": gastos_entretenimento,
        "valor_medio_entretenimento": valor_medio_entretenimento,
        "padrao_consumo_servicos": padrao_consumo_servicos,
        "valor_medio_pcs": valor_medio_pcs,
        "gastos_educ_saude": gastos_educ_saude,
        "valor_medio_educ_saude": valor_medio_educ_saude,
        "principais_cartoes": principais_cartoes,
        "forma_pagamento_comum": forma_pagamento_comum
    }
    
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    
    return "Usuario criado com sucesso!"

def ler_usuarios():
    usuarios = carregar_usuarios()
    if usuarios:
        for pessoa in usuarios:
            print(f"nome: {pessoa['username']}")
            print(f"cpf: {pessoa['cpf']}")
            print(f"idade: {pessoa['idade']}")
            print(f"genero: {pessoa['genero']}")
            print(f"email: {pessoa['email']}")
            print(f"password: {pessoa['password']}")
            print(f"renda_mensal: {pessoa['renda_mensal']}")
            print(f"fontes_renda_principais: {pessoa['fontes_renda_principais']}")
            print(f"categorias_despesas: {pessoa['categorias_despesas']}")
            print(f"despesas_mensais: {pessoa['despesas_mensais']}")
            print(f"valor_medio_despesas_mensais: {pessoa['valor_medio_despesas_mensais']}")
            print(f"dividas_pendentes: {pessoa['dividas_pendentes']}")
            print(f"valor_medio_dividas_pendentes: {pessoa['valor_medio_dividas_pendentes']}")
            print(f"capacidade_poupanca: {pessoa['capacidade_poupanca']}")
            print(f"objetivos_curto_prazo: {pessoa['objetivos_curto_prazo']}")
            print(f"objetivos_medio_prazo: {pessoa['objetivos_medio_prazo']}")
            print(f"objetivos_longo_prazo: {pessoa['objetivos_longo_prazo']}")
            print(f"gastos_entretenimento: {pessoa['gastos_entretenimento']}")
            print(f"valor_medio_entretenimento: {pessoa['valor_medio_entretenimento']}")
            print(f"padrao_consumo_servicos: {pessoa['padrao_consumo_servicos']}")
            print(f"valor_medio_pcs: {pessoa['valor_medio_pcs']}")
            print(f"gastos_educ_saude: {pessoa['gastos_educ_saude']}")
            print(f"valor_medio_educ_saude: {pessoa['valor_medio_educ_saude']}")
            print(f"principais_cartoes: {pessoa['principais_cartoes']}")
            print(f"forma_pagamento_comum: {pessoa['forma_pagamento_comum']}")
        return "Nenhum usuario encontrado."
    return usuarios

def atualizar_usuarios(cpf, new_password):
    usuarios = carregar_usuarios()
    
    if cpf not in usuarios:
        return "Usuario nao encontrado!"
    
    usuarios[cpf]['password'] = new_password
    salvar_usuarios(usuarios)
    return "Senha atualizada com sucesso!"

def deletar_usuarios(cpf):
    usuarios = carregar_usuarios()
    
    if cpf not in usuarios:
        return "Usuario nao encontrado!"
    
    del usuarios[cpf]
    salvar_usuarios(usuarios)
    return "Usuario deletado com sucesso!"

def login(cpf, password):
    usuarios = carregar_usuarios()
    
    cpf = cpf.strip()
    password = password.strip()
    
    for i in usuarios:
        if str(i["cpf"]) == cpf and str(i["password"]) == password:
            return "Login bem-sucedido!"
        else:
            return "Senha incorreta ou cpf incorreto!"     
    
def menu():
    while True:
        print("\n---> FinSolucoes <---")
        print("1 - Criar usuario")
        print("2 - Ler usuarios")
        print("3 - Atualizar senha")
        print("4 - Deletar usuario")
        print("5 - Login")
        print("0 - Sair")
        
        option = input("Escolha uma opcao: ")
        
        if option == '1':
            username = input("Nome de usuario: ")
            cpf = input("informe o cpf: ")
            idade = input("Data de nascimento: ")
            genero = input("Informe o genero: (M/F) ")
            email = input("Email de contato: ")
            password = input("Senha: ")
            renda_mensal = input("informa sua renda mensal: ")
            fontes_renda_principais = input("informa suas principais fontes de renda: ")
            categorias_despesas = input("agora as categorias das despesas: ")
            despesas_mensais = input("informe suas despesas mensais: ")
            valor_medio_despesas_mensais = input("informe o valor medio das suas despesas mensais: ")
            dividas_pendentes = input("informe se voce possui dividas pendentes: (Se nao possui, digite *0* )")
            valor_medio_dividas_pendentes = input("informe o valor medio das suas dividas pendentes: (Se nao possui, digite *0* )")
            capacidade_poupanca = input("informe a capacidade da sua poupança: ")
            objetivos_curto_prazo = input("informe quais sao seus objetivos a curto prazo: ")
            objetivos_medio_prazo = input("informe quais sao seus objetivos a medio prazo: ")
            objetivos_longo_prazo = input("informe quais sao seus objetivos a longo prazo: ")
            gastos_entretenimento = input("informe seus gastos com entreterimento em geral: ")
            valor_medio_entretenimento = input("informe os gastos medios com entreterimento: ")
            padrao_consumo_servicos = input("qual o padrao de consumo com os servicos: ")
            valor_medio_pcs = input("informe o valor medio pcs: ")
            gastos_educ_saude = input("informe o valor com os gastos de educacao e saude: ")
            valor_medio_educ_saude = input("qual o valor medio dos gastos de educacao e saude: ")
            principais_cartoes = input("informe seus principais cartoes: ")
            forma_pagamento_comum = input("informe qual a forma de pagamento que voce costuma usar: ")
            print(criar_usuarios(username, cpf, idade, genero, email, password, renda_mensal, fontes_renda_principais, categorias_despesas, despesas_mensais, valor_medio_despesas_mensais, dividas_pendentes, valor_medio_dividas_pendentes, capacidade_poupanca, objetivos_curto_prazo, objetivos_medio_prazo, objetivos_longo_prazo, gastos_entretenimento, valor_medio_entretenimento, padrao_consumo_servicos, valor_medio_pcs, gastos_educ_saude, valor_medio_educ_saude, principais_cartoes, forma_pagamento_comum))
        
        elif option == '2':
            ler_usuarios()
        
        elif option == '3':
            cpf = input("informe o cpf do usuario: ")
            new_password = input("Nova senha: ")
            print(atualizar_usuarios(cpf, new_password))
        
        elif option == '4':
            cpf = input("informe o cpf do usuario: ")
            print(deletar_usuarios(cpf))
        
        elif option == '5':
            cpf = input("informe o cpf do usuario: ")
            password = input("Senha: ")
            print(login(cpf, password))
        
        elif option == '0':
            print("Voltando...")
            break
        
        else:
            print("Opcao invalida!")
            
menu()