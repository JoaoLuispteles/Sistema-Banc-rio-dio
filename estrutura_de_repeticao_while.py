opcao = -1

while opcao != 0:
    opcao = (input("[1] Sacar \n[2] Extrato \n[3] Sair \n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por utilizar nosso Sistema, até logo!")