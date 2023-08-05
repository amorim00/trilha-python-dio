menu = """
================ MENU ================

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

    if opcao == "d":
        valor = float(input("Informe o valor do depósito!"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
          print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque!"))

        if valor > 0 and saldo > valor and valor <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        elif valor > saldo:
            print("Operação falhou, você não tem saldo suficiente!")
        elif valor > limite:
            print("Operação falhou, o valor do saque exede o limite!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou, número de saques diarios exedidos!")
        else:
          print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")