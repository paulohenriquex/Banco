from ContaBancaria import ContaBancaria
from Depositar import Depositar
from Sacar import Sacar
from Mostrarsaldo import Mostrarsaldo


def Main():

    cliente = None

    while True:
        print("1 - Cadastrar cliente")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Mostrar")
        print("0 - Sair")
        opcao = int(input())
        if opcao == 1:
            cliente = ContaBancaria.Cadastrar_Cliente()
        if opcao == 2:
            valor = float(input("Digite o valor a ser depositado: "))
            Depositar(cliente, valor)
        elif opcao == 3:
            valor = float(input("Digite o valor a ser sacado: "))
            Sacar(cliente, valor)
        elif opcao == 4:
            if cliente:
                Mostrarsaldo(cliente)
            else:
                print("Cliente não cadastrado.")
        elif opcao == 0:
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    Main()
