def Sacar(cliente, valor):
    if valor <= cliente.saldo:
        cliente.saldo -= valor
    else:
        print("Saldo insuficiente.")
