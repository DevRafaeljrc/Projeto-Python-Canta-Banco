menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Pagar Fatura
[5] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Entre com o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha no Depósito! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Entre com o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo invalido! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Ultrapassou o valor permitido! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Saque diario excedido! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Entre com uma valor válido! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        valor = float(input("Entre com o valor da fatura: "))
        if valor > 0:
            saldo -= valor
            extrato += f"Pagamento de fatura: R$ {valor:.2f}\n"
            print("Fatura paga com sucesso!")
        else:
            print("Falha no pagamento! O valor informado é inválido.")


    elif opcao == "5":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        print("Se as nãos opções acima não forem suficientes, entre em contato com o suporte.")
        print("Agradecemos por utilizar nosso sistema de gerenciamento de contas bancárias.")