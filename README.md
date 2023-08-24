# Desafio  Kotlin Com Exemplos: Desafio de Projeto (Lab)

Desafio de Projeto permite que o usuário faça depósitos em contas específicas caso o CPF esteja cadastrado. Também é possível realizar saques sujeitos ao limite diário de três saques, de até R$ 500,00 cada. Além disso, o sistema exibe o extrato da conta, mostrando movimentações, saldo atualizado e informações do titular.
O cadastro do usuário é feito por meio de nome, data de nascimento, CPF e endereço. Aplicam-se restrições para evitar CPFs duplicados e entradas de dados inválidas. As contas são cadastradas com número de agência, número de conta e vinculadas ao usuário por meio do CPF.

Por fim, o sistema permite uma listagem de todas as contas cadastradas, indicando o número da agência, número da conta e nome do titular.

Foi um belo desafio implementar este sistema bancário em Python!

## 🚀 Desafio

```
Modelando o Sistema Bancário em POO com Python 😉"
```

# 🔧 Apresentação do código

***Parte 1:*** Classe Usuario e Classe Conta

````
class Usuario:
    def __init__(self, nome, data_de_nascimento, cpf, endereco):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.endereco = endereco
````
A classe Usuario representa um usuário com atributos como nome, data de nascimento, CPF e endereço.
``````
class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0.0
        self.transacoes = []
        self.num_saque = 0  # Variável para rastrear o número de saques
``````
A classe Conta representa uma conta bancária com atributos como agência, número da conta, usuário associado, saldo, lista de transações e um contador para o número de saques feitos.

***Parte 2:*** Métodos da Classe Conta

```
    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito: + R$ {valor:.2f}")
        print(f"\n===> Depósito de R$ {valor:.2f} realizado com sucesso <===")
```
O método depositar permite que o usuário deposite dinheiro na conta. Ele atualiza o saldo da conta, adiciona a transação de depósito à lista de transações e imprime uma mensagem de sucesso.

```
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
```
O método sacar permite que o usuário faça saques da conta. Ele verifica se o limite máximo de saques para o dia foi atingido, se o valor do saque excede o limite e se há fundos suficientes na conta. Se todas as condições forem atendidas, ele atualiza o saldo da conta, adiciona a transação de saque à lista de transações, incrementa a contagem de saques e imprime uma mensagem de sucesso.

```
    def extrato(self):
        if not self.transacoes:
            return "\n===> Nenhuma transação registrada. <==="
        extrato = "\n******** EXTRATO ********\n"
        extrato += f"Nome: {self.usuario.nome}\n"
        extrato += f"Número da Conta: {self.numero_conta}\n"
        for transacao in self.transacoes:
            extrato += f"{transacao}\n"
        extrato += f"\nSaldo Atual: R$ {self.saldo:.2f}\n"  # Adiciona uma quebra de linha
        extrato += "******** FIM **********"  # Adiciona a linha abaixo do campo
        return extrato
```
O método extrato retorna uma string formatada que representa o extrato da conta. Ele verifica se existem transações na lista. Se não houver transações, ele retorna uma mensagem indicando que não há transações registradas. Caso contrário, ele cria uma string com o nome do usuário, número da conta e todas as transações na lista, seguidas pelo saldo da conta atual.

***Parte 3:*** Classe Banco

```
class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.contador_contas = 1
```
A classe Banco representa um banco com atributos como listas de usuários e contas, e um contador para a criação de contas.

```
    def encontrar_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None
```
O método encontrar_usuario_por_cpf recebe um CPF como entrada e procura por um usuário correspondente na lista de usuários. Se uma correspondência for encontrada, ele retorna o objeto do usuário; caso contrário, retorna None.

```
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
```
O método criar_conta recebe um CPF como entrada e cria uma nova conta bancária associada ao usuário correspondente ao CPF. Ele verifica se o usuário existe e se o CPF do usuário já está associado a uma conta. Se uma das condições não for atendida, ele imprime uma mensagem de erro. Caso contrário, ele cria um novo objeto de conta com um número de agência fictício, o número de conta atual a partir do contador e o objeto de usuário associado. Em seguida, adiciona a conta à lista de contas e incrementa o contador.

***Parte 4:*** Funções de validação e interação com o usuário

```
def is_valid_cpf(cpf):
    return cpf.isnumeric()

def is_valid_name(name):
    return all(char.isalpha() or char.isspace() for char in name)

def is_valid_date(date):
    return date.replace("/", "").isnumeric()
```
A função is_valid_cpf verifica se um determinado CPF consiste apenas em dígitos numéricos. A função is_valid_name verifica se um nome consiste apenas em caracteres alfabéticos e espaços. A função is_valid_date verifica se uma data consiste apenas em dígitos numéricos e barras.

```
def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    while not is_valid_name(nome):
        print("===> Nome inválido. Digite apenas nome e sobrenome. <===")
        nome = input("Digite seu nome: ")

    data_de_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    while not is_valid_date(data_de_nascimento):
        print("===> Data de nascimento inválida. Digite uma data válida! <===.")
        data_de_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

    cpf = input("Digite seu CPF: ")
    while not is_valid_cpf(cpf):
        print("===> CPF inválido. Digite apenas números. <===")
        cpf = input("Digite seu CPF: ")

    endereco = input("Digite seu endereço: ")
    usuario = Usuario(nome, data_de_nascimento, cpf, endereco)
    banco.usuarios.append(usuario)
    print("\n===> Usuário cadastrado com sucesso! <===")
```
A função cadastrar_usuario solicita ao usuário que digite seu nome, data de nascimento, CPF e endereço. Ela valida cada entrada e cria um novo objeto Usuario com os dados fornecidos. O novo objeto de usuário é adicionado à lista de usuários do banco.

```
def depositar():
    cpf = input("Digite o CPF para depósito: ")
    while not is_valid_cpf(cpf):
        print("===> CPF inválido. Digite apenas números. <===")
        cpf = input
```

## 📦 Implementação

Completar todo o código

## 🛠️ Construído com

* [Visual Studio Code](https://code.visualstudio.com/download) - Code Editing


## ✒️ Autores


* **Rodrigo Neris** -  [*Trabalho Inicial*](https://github.com/rodrigonerisalves)
---
⌨️ com ❤️ por [Rodrigo Neris](www.linkedin.com/in/rodrigo-neris) 😊