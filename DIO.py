saldo = 0
saques_diarios = 3
limite_saques = 500
saques_realizados = []

while True:
    print("\nOpções:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Visualizar Extrato")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Digite o valor para depositar: "))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${saldo:.2f}")
        else:
            print("Valor inválido para depósito.")
    elif opcao == 2:
        valor = float(input("Digite o valor para sacar: "))
        if saques_diarios > 0 and valor <= limite_saques:
            if valor <= saldo:
                saldo -= valor
                saques_diarios -= 1
                saques_realizados.append(-valor)
                print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Limite diário de saques atingido ou valor de saque inválido.")
    elif opcao == 3:
        print("Extrato:")
        for i, saque in enumerate(saques_realizados, start=1):
            print(f"{i}. Saque de R${-saque:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == 4:
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
