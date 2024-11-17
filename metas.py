import json
import os

arquivo = "metas.json"

def carregar_metas():
    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r") as infile:
                return json.load(infile)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return []
    return []

def salvar_metas(metas):
    with open(arquivo, 'w') as file:
        json.dump(metas, file, indent=4)   
        
def criar_metas(nome, prazo, descricao):
    metas = carregar_metas()
    
    nova_meta = {
        "nome": nome,
        "prazo": prazo,
        "descrição": descricao,
    }
    
    metas.append(nova_meta)
    salvar_metas(metas)
    
    return "Meta criada com sucesso!"

def listar_metas():
    metas = carregar_metas()
    if metas:
        for meta in metas:
            print(f"nome: {meta['nome']}")
            print(f"prazo: {meta['prazo']}")
            print(f"descrição: {meta['descrição']}")
        return "Nenhuma meta encontrada."
    return metas

def atualizar_meta(nome_antigo, novo_nome, prazo, novo_prazo, descricao, nova_descricao):
    metas = carregar_metas()
    
    for meta in metas:
        if meta['nome'] == nome_antigo:
          meta[nome_antigo]['nome'] = novo_nome
          meta[prazo]['prazo'] = novo_prazo
          meta[descricao]['descrição'] = nova_descricao
          break

    salvar_metas(metas)
    return "Meta atualizada!"

def deletar_meta(nome):
    metas = carregar_metas()
    
    for meta in metas:  
        if meta['nome'] == nome:
            metas.remove(meta)

    salvar_metas(metas)
    return "Meta deletada com sucesso!"
    
def menu():
    print("\n---> FinSolucoes <---")
    print("1 - Criar meta")
    print("2 - Listar meta")
    print("3 - Atualizar meta")
    print("4 - Deletar meta")
    print("5 - Voltar ao menu anterior")
        
    option = input("Escolha uma opcao: ")
        
    if option == '1':
        nome = input("Nome da meta: ")
        prazo = input("Informe se o prazo é curto, médio ou longo: ")
        descricao = input("Digite uma descrição para sua meta: ")
        print(criar_metas(nome, prazo, descricao))    
    elif option == '2':
        listar_metas()    
    elif option == '3':
        nome_antigo = input("informe o nome da meta: ")
        novo_nome = input("Digite o novo nome para sua meta:")
        novo_prazo = input("Digite se o novo prazo é curto, médio ou longo: ")
        nova_descricao = input("Digite uma nova descrição:")
        print(atualizar_meta(nome_antigo, novo_nome, novo_prazo, nova_descricao))    
    elif option == '4':
        nome = input("Digite nome da meta a ser deletada: ")
        print(deletar_meta(nome))         
    elif option == '0':
        print("Voltando...")  
    else:
        print("Opcao invalida!")           

