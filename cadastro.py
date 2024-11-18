import json
import os

arquivo = "usuarios.json"

def carregar_usuarios():
    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r") as infile:
                dados = json.load(infile)
                if isinstance(dados, list):
                    return dados
                else:
                    return []
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return []
    return []

def salvar_usuarios(usuarios):
    with open(arquivo, 'w') as file:
        json.dump(usuarios, file, indent=4)

def criar_usuarios(username, cpf, idade, genero, email, password):
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return "Usuário já existe!"

    novo_usuario = {
        "username": username,
        "cpf": cpf,
        "idade": idade,
        "genero": genero,
        "email": email,
        "password": password
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)

    return "Usuário criado com sucesso!"

def ler_usuarios():
    usuarios = carregar_usuarios()
    if usuarios:
        for pessoa in usuarios:
            print(f"Nome: {pessoa['username']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"Gênero: {pessoa['genero']}")
            print(f"Email: {pessoa['email']}")
            print(f"Password: {pessoa['password']}\n")
        return "Usuários listados acima."
    else:
        return "Nenhum usuário encontrado."

def atualizar_usuarios(cpf, novo_username, nova_idade, novo_genero, novo_email, nova_senha):
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario['username'] = novo_username
            usuario['idade'] = nova_idade
            usuario['genero'] = novo_genero
            usuario['email'] = novo_email
            usuario['password'] = nova_senha
            salvar_usuarios(usuarios)
            return "Usuário atualizado com sucesso!"
    
    return "Usuário não encontrado!"

def deletar_usuarios(cpf):
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            salvar_usuarios(usuarios)
            return "Usuário deletado com sucesso!"
    
    return "Usuário não encontrado!"

def login(cpf, password):
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["password"] == password:
            return "Login bem-sucedido!"
    
    return "CPF ou senha incorretos!"

def menu_cadastro():
    while True:
        print("\n---> FinSolucoes <---")
        print("1 - Criar usuário")
        print("2 - Ler usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("5 - Login")
        print("0 - Sair")
        
        option = input("Escolha uma opção: ")
        
        if option == '1':
            username = input("Nome de usuário: ")
            cpf = input("Informe o CPF: ")
            idade = input("Informe sua idade: ")
            genero = input("Informe o gênero: (M/F) ")
            email = input("Email de contato: ")
            password = input("Senha: ")
            print(criar_usuarios(username, cpf, idade, genero, email, password))
        
        elif option == '2':
            print(ler_usuarios())
        
        elif option == '3':
            cpf = input("Informe o CPF do usuário: ")
            novo_username = input("Atualizar nome do usuário: ")
            nova_idade = input("Atualizar idade do usuário: ")
            novo_genero = input("Atualizar gênero do usuário: (M/F) ")
            novo_email = input("Atualizar email do usuário: ")
            nova_senha = input("Atualizar senha do usuário: ")
            print(atualizar_usuarios(cpf, novo_username, nova_idade, novo_genero, novo_email, nova_senha))
        
        elif option == '4':
            cpf = input("Informe o CPF do usuário: ")
            print(deletar_usuarios(cpf))
        
        elif option == '5':
            cpf = input("Informe o CPF do usuário: ")
            password = input("Senha: ")
            print(login(cpf, password))
        
        elif option == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")
