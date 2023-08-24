class Usuario:
    def __init__(self, nome, data_de_nascimento, cpf, endereco):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0.0
        self.transacoes = []
        self.num_saque = 0  # Variável para rastrear o número de saques

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito: + R$ {valor:.2f}")
        print(f"\n===> Depósito de R$ {valor:.2f} realizado com sucesso <===")
    
    def sacar(self, valor):
        if self.num_saque >= 3:  # Verifica se já atingiu o limite de saques
            print("\n===> Você atingiu o número máximo de saques para hoje. <===")
            return
        if valor > 500.0:
            print("\n===> Você só pode sacar até R$ 500,00 por vez. <===")
            return
        if self.saldo < valor:
            print("\n===> Saldo insuficiente. <===")
            return
        self.saldo -= valor
        self.transacoes.append(f"Saque: - R$ {valor:.2f}")
        self.num_saque += 1  # Incrementa o número de saques realizados
        print(f"\n===> Saque de R$ {valor:.2f} realizado com sucesso! <===")

    def extrato(self):
        if not self.transacoes:
            return "\n===> Nenhuma transação registrada. <==="
        extrato = "\n******** EXTRATO ********\n"
        extrato += f"Nome: {self.usuario.nome}\n"
        extrato += f"Número da Conta: {self.numero_conta}\n"
        for transacao in self.transacoes:
            extrato += f"{transacao}\n"
        extrato += f"\nSaldo Atual: R$ {self.saldo:.2f}\n"  # Add a newline character
        extrato += "******** FIM **********"  # Add the line below the field
        return extrato


class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.contador_contas = 1

    def encontrar_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_conta(self, cpf):
        usuario = self.encontrar_usuario_por_cpf(cpf)
        if usuario is None:
            print("\n===> Por favor, registre um usuário. <===")
            return
        if any(conta.usuario.cpf == cpf for conta in self.contas):
            print("\n===> CPF já está associado a uma conta. <===")
            return
        print("\n===> Conta cadastrada com sucesso! <===")
        conta = Conta("0001", self.contador_contas, usuario)
        self.contas.append(conta)
        self.contador_contas += 1

    def listar_contas(self):
        if not self.contas:
            print("\n===> Conta sem movimentação <===")
            return

        print("\n******** CONTAS ********")
        for conta in self.contas:
            print(f"Agência: {conta.agencia} - Número da Conta: {conta.numero_conta}")
            print(f"Usuário: {conta.usuario.nome}")
            print("************************")


def is_valid_cpf(cpf):
    return cpf.isnumeric()


def is_valid_name(name):
    return all(char.isalpha() or char.isspace() for char in name)


def is_valid_date(date):
    return date.replace("/", "").isnumeric()


def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    while not is_valid_name(nome):
        print("===> Nome inválido. Digite apenas nome e sobrenome. <===")
        nome = input("Digite seu nome: ")

    data_de_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    while not is_valid_date(data_de_nascimento):
        print("===> Data de nascimento inválida. Digite uma data! <===.")
        data_de_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

    cpf = input("Digite seu CPF: ")
    while not is_valid_cpf(cpf):
        print("===> CPF inválido. Digite apenas números. <===")
        cpf = input("Digite seu CPF: ")

    endereco = input("Digite seu endereço: ")
    usuario = Usuario(nome, data_de_nascimento, cpf, endereco)
    banco.usuarios.append(usuario)
    print("\n===> Usuário cadastrado com sucesso <===")


def is_valid_number(number):
    return number.isnumeric()


def depositar():
    cpf = input("Digite o CPF para depósito: ")
    while not is_valid_cpf(cpf):
        print("===> CPF inválido. Digite apenas números.<===")
        cpf = input("Digite o CPF para depósito: ")

    conta = None
    for c in banco.contas:
        if c.usuario.cpf == cpf:
            conta = c
            break

    if conta is None:
        print("\n===> Por favor, registre um usuário. <===.")
        return

    valor = input("Digite o valor do depósito: ")
    while not is_valid_number(valor):
        print("===> Valor inválido. Digite apenas números. <===")
        valor = input("Digite o valor do depósito: ")

    conta.depositar(float(valor))


def sacar():
    cpf = input("Digite o CPF para saque: ")
    while not is_valid_cpf(cpf):
        print("===> CPF inválido. Digite apenas números. <===")
        cpf = input("Digite o CPF para saque: ")

    conta = None
    for c in banco.contas:
        if c.usuario.cpf == cpf:
            conta = c
            break

    if conta is None:
        print("\n===> Por favor, registre um usuário. <===.")
        return

    valor = input("Digite o valor do saque: ")
    while not is_valid_number(valor):
        print("===> Valor inválido. Digite apenas número. <===.")
        valor = input("Digite o valor do saque: ")

    conta.sacar(float(valor))


def extrato():
    cpf = input("Digite o CPF para consultar o extrato: ")
    while not is_valid_cpf(cpf):
        print("===> CPF inválido. Digite apenas números. <===")
        cpf = input("Digite o CPF para consultar o extrato: ")

    conta = None
    for c in banco.contas:
        if c.usuario.cpf == cpf:
            conta = c
            break

    if conta is None:
        print("\n===> Por favor, registre um usuário. <===.")
        return

    extrato = conta.extrato()
    print(extrato)


def menu():
    while True:
        print()
        print("********** MENU **********")
        print("[1] \tDEPOSITAR")
        print("[2] \tSACAR")
        print("[3] \tEXTRATO")
        print("[4] \tCADASTRAR USUÁRIO")
        print("[5] \tCADASTRAR CONTA")
        print("[6] \tLISTAR CONTA")
        print("[7] \tSAIR")
        escolha = input("Selecione uma opção: ")
        if escolha == "1":
            depositar()
        elif escolha == "2":
            sacar()
        elif escolha == "3":
            extrato()
        elif escolha == "4":
            cadastrar_usuario()
        elif escolha == "5":
            cpf = input("Digite o CPF para criar uma conta: ")
            banco.criar_conta(cpf)
        elif escolha == "6":
            banco.listar_contas()
        elif escolha == "7":
            break


banco = Banco()
menu()
