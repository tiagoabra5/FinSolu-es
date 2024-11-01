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
        
def criar_usuarios(username, cpf, idade, genero, email, password):
    usuarios = carregar_usuarios()
    
    if cpf in usuarios:
        return "Usuario ja existe!"
    
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
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["password"] == password:
            return print("Login bem-sucedido!")
        else:
            return print("CPF ou senha incorretos!")

#def login(cpf, password):
#    usuarios = carregar_usuarios()
#    
#    cpf = cpf.strip()
#    password = password.strip()
#    
#    for i in usuarios:
#        if str(i["cpf"]) == cpf and str(i["password"]) == password:
#            return "Login bem-sucedido!"
#        else:
#            return "Senha incorreta ou cpf incorreto!"     
    
def menu():
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
        print(criar_usuarios(username, cpf, idade, genero, email, password))
        
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
        
    else:
        print("Opcao invalida!")           