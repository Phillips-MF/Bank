import datetime as dt
saldo = 0
extrato = []
deposito = 0
saldo = float(input("Digite o seu saldo atual: "))
saque_diario = 3
while True:
    print("seu saldo atual é: R$", saldo)
    opcao = input(""" 
                  Selecione as seguintes opções.
                      d -> Depositar
                      s -> Sacar
                      e -> Extrato
                      q -> Sair
                      
                  """)
    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: R$"))
        if valor <= 0:
            print("""O valor a ser depositado precisa ser maior que zero!!!""")
        elif valor > 0:
            saldo += valor
            print("Depósito de: R$", valor, " realizado com sucesso!")
            registro = "Depósito de: R${} - {}".format(valor, dt.datetime.now())
            extrato.append(registro)
    
    elif opcao == "s":
        print("Quantidade de saques diários: ", saque_diario)
        if saque_diario == 0:
            print("Só é possível realizar 3 saques diários!!!")    
        else:
            valor = float(input("Digite o valor para saque: R$"))
            if valor <= 0:
                print("""Valor invávlido!\n 
                      O valor precisa ser maior que zero!!!""")
            elif valor > saldo:
                print("""Valor inválido!\n
                      Você não possui saldo o suficiente para sacar esse valor!""")
            else:
                saldo -= valor
                print("Saque de: R$", valor, " realizado com sucesso!")
                registro = "Saque de: R${} - {}".format(valor, dt.datetime.now())
                extrato.append(registro)
                saque_diario -= 1
    
    elif opcao == "e":
        for n in range(len(extrato)):
            print(extrato[n])
            
    elif opcao == "q":
        print("Até mais tarde!")
        break
    else:
        print("Opção inválida, por favor selecione uma das opções disponíveis")