def menu(): 
    menu = """\n
========== MENU ==========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta 
[6] Listar conta
[7] Sair
=> """

    return input(menu)

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("O valor do depósito precisa ser maior que 0!")

    return saldo, extrato

def sacar(*, valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
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
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("O valor do saque precisa ser maior que 0!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== Extrato ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================") 

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return 
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro-nro-bairro-cidade-UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,  "cpf": cpf,  "endereço": endereco })
    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, usuarios, numero_conta):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com Sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
             Agência: {conta['agencia']}
             C/C: {conta['numero_conta']}
             Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
   
   LIMITE_SAQUES = 3
   AGENCIA = "0001"

   saldo = 0
   limite = 500
   extrato = ""
   numero_saques = 0
   usuarios = []
   contas = []

   while True:

    opcao =menu()

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: R$ "))

        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        saldo, extrato, = sacar(
            valor=valor,
            saldo=saldo,
            extrato=extrato,
            numero_saques=numero_saques,
            limite=limite,
            LIMITE_SAQUES=LIMITE_SAQUES
        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, usuarios, numero_conta)

        if conta:
            contas.append(conta)

    elif opcao == "6":
        listar_contas(contas)
    
    elif opcao == "7":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
