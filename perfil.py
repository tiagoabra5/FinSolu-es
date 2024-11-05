import json
# pelo que testei cada vez que se adiciona um perfil diferente o outro é excluido @andre e @maju, tentem ver se consegue fazer o perfil de gastos ser vinculado diretamente com o perfil do usuario(cadastro)
arquivo = "perfil.json"

def salvar_perfil_usuario(perfil_usuario):
    with open(arquivo, 'w') as file:
        json.dump(perfil_usuario, file, indent=4)
    print("Perfil do usuário salvo com sucesso!")
# função com todas as perguntas que precisam ser respondidas, ainda acho que são muitas mas ok
def criar_perfil_usuario():
    perfil_usuario = {
        "renda_mensal": float(input("Informe sua renda mensal: ")),
        "fontes_renda_principais": input("Informe suas principais fontes de renda: "),
        "valor_medio_despesas_mensais": float(input("Informe o valor médio das despesas mensais: ")),
        "dividas_pendentes": input("Descreva suas dívidas pendentes: "),
        "valor_medio_dividas_pendentes": float(input("Informe o valor médio das dívidas pendentes: ")),
        "capacidade_poupanca": float(input("Informe sua capacidade de poupança: ")),
        "objetivos_curto_prazo": input("Quais são seus objetivos de curto,médio e longo prazo? "),
        "gastos_entretenimento": input("Descreva seus gastos com entretenimento: "),
        "valor_medio_entretenimento": float(input("Informe o valor médio de gastos com entretenimento: ")),
        "padrao_consumo_servicos": input("Descreva seu padrão de consumo de serviços: "),
        "valor_medio_pcs": float(input("Informe o valor médio de consumo de serviços: ")),
        "gastos_educ_saude": input("Descreva seus gastos com educação e saúde: "),
        "valor_medio_educ_saude": float(input("Informe o valor médio dos gastos com educação e saúde: ")),
        "principais_cartoes": input("Informe seus principais cartões de crédito: "),
        "forma_pagamento_comum": input("Informe sua forma de pagamento mais comum: ")      
    }
    
    salvar_perfil_usuario(perfil_usuario)

# msg de quando inicia lá pelo menu
def menu():
    print("Bem-vindo ao módulo de Perfil Financeiro!")
    criar_perfil_usuario()
