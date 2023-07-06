def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def depositar(conta, valor):
    conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("numero: {} \ntitular: {} \nsaldo: {}".format(conta['numero'], conta['titular'], conta['saldo']))

conta1 = cria_conta('123-4', 'Pedro Salles', 1000.0, 10000.0)
conta1['saldo'] = 1000000.0
depositar(conta1, 1000.0)
extrato(conta1)

sacar(conta1, 500.0)
extrato(conta1)