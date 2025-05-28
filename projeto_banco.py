
import textwrap
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        conta = cls(numero, cliente)
        cliente.adicionar_conta(conta)
        return conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False
        elif valor > self._saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False
        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([
            t for t in self.historico.transacoes if t["tipo"] == "Saque"
        ])

        if numero_saques >= self.limite_saques:
            print("\n@@@ Operação falhou! Limite de saques atingido. @@@")
            return False
        elif valor > self.limite:
            print("\n@@@ Operação falhou! Valor excede o limite. @@@")
            return False
        return super().sacar(valor)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
        })


class Transacao(ABC):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


def menu():
    menu = """\n
=============== MENU ===============
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário
[q]\tSair
=> """
    return input(textwrap.dedent(menu))

def filtrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u.cpf == cpf), None)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ")

    usuario = PessoaFisica(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    print("\n=== Usuário criado com sucesso! ===")

def criar_conta(numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado. @@@")
        return

    conta = ContaCorrente.nova_conta(usuario, numero_conta)
    print("\n=== Conta criada com sucesso! ===")
    return conta

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta.agencia}
        C/C:\t\t{conta.numero}
        Titular:\t{conta.cliente.nome}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            print(f"{transacao['tipo']}:\tR$ {transacao['valor']:.2f}")

    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")

def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            usuario = filtrar_usuario(cpf, usuarios)

            if not usuario:
                print("\n@@@ Usuário não encontrado. @@@")
                continue

            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            transacao.registrar(usuario.contas[0])

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            usuario = filtrar_usuario(cpf, usuarios)

            if not usuario:
                print("\n@@@ Usuário não encontrado. @@@")
                continue

            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            transacao.registrar(usuario.contas[0])

        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            usuario = filtrar_usuario(cpf, usuarios)

            if not usuario:
                print("\n@@@ Usuário não encontrado. @@@")
                continue

            exibir_extrato(usuario.contas[0])

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida! Tente novamente. @@@")

if __name__ == "__main__":
    main()
