conta_noraml = False
conta_universitaria = False

saldo = 2000
saque = 2400
cheque_especial = 450

if conta_noraml:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, Saldo Insuficiente!") 
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo Insuficiente!")
else:
    print("O sistema não reconheceu seu tipo de conta corrente, entre em contato com seu gerente.")