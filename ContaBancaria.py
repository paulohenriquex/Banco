

class ContaBancaria:
    def __init__(self, nome, agencia, conta, saldo):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @staticmethod
    def Cadastrar_Cliente():
        nome = input("Digite o nome do cliente: ")
        agencia = int(input("Digite a agencia: "))
        conta = int(input("Digite o numero da conta: "))
        saldo = float(input("Digite o saldo inicial da conta: "))

        return ContaBancaria(nome, agencia, conta, saldo)
