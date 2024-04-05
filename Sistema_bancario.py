menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor a ser depositado: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Operação Falhou!")


    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Falha!!!\nSaldo insuficiente")

        elif excedeu_limite:
            print("Falha!!!\nO valor do saque ultrapassou o limite por saque!")
        
        elif excedeu_saque:
            print("Falha!!!\n A quantidade de saques chegou ao limite!")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_de_saques += 1
        
        else:
            print("Operação Falhou!")
    
    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:R${saldo:.2f}")
        print("=====================================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")







