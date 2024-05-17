menu = """
[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    #condição
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: AKZ"))
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        
        else:
            print("Valor inválido")
    
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: AKZ"))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo or excedeu_limite or excedeu_saques:
            print("Operação falhou! você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("operação falhou! O valor saques excede o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor >0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Valor informado é inválido")
            
    elif opcao == "e":
        print("\n-------------------Extrato---------------------------")
        print("Não forma realizados movimentação. " if not extrato else extrato)
        print(f"\nSaldo: AKZ {saldo:.2f}")
        print("----------------------------------------------------")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação Inválido, por favor selecione novamente a operação desejado.")
        
        