
def menu()
    print("----> Bem vindo a simulação da finsoluções <----")
    print("1 - Simular Tesouro Direto selic 12,75% ao ano")
    print("2 - Simular CDB fixo com 10,97% ao ano")
    print("3 - Simular LCI com direito a 11% ao ano")
    print("4 - Simular Fundos de renda fixa com direito a 12% ao ano")

def calculo1(valorinicial, tempo, taxaMensal, aporteMensal= 0):
    montante = valorinicial 
    for mes in range (1, tempo + 1 ) 
     montante *= ( 1+ taxaMensal) 
     if aporteMensal > 0:
        montante += aporteMensal
    return montante
def menu()
opcao = int(input("Insira qual simulação deseja fazer"))
match (opcao):
    case 1:
        valorinicial = float(input("Insira o capital inicial que deseja investir: "))
        tempo = int(input("Insira o tempo em meses que deseja aplicar o dinheiro: "))
        aporteMensal = float(input("Caso queira realizar aportes mensais insira o valor caso contrario digite 0: "))
        taxaAnual = 12,75/100
        taxaMensal = (1 + taxaAnual) **(1/12) - 1
        montanteFinal= calculo1(valorinicial,tempo, taxaMensal, aporteMensal)
        
        print("f\n Apos", tempo," apos implementar um capital inicial de ", valorinicial," reais e aportes mensais de ", aporteMensal," o total obtido foi de ",montanteFinal )


    



