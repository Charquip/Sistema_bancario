menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        valor = float(input("Digite o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Saldo: R$ {valor:.2f}\n"

        else:
            print("O valor do depósito precisa ser maior que 0!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Parece que seu saldo não é suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Parece que seu limite não é suficiente.")

        elif excedeu_saques:
            print("Operação falhou! Seu limite de saques diários expirou, tente novamente amanhã.")
        
        elif valor > 0:
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numero_saques += 1

        else:
            print("O valor do saque precisa ser maior que 0!")

    elif opcao == "3":
        print("\n========== Extrato ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print  ("=============================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
