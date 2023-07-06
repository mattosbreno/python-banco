from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Maicon', 'Kuster', '12345678-00')
cliente2 = Cliente('Enzo', 'Vasconcelos', '54361239-00')
cliente3 = Cliente('Maria', 'Souza', '87654321-00')

conta1 = Conta('123-4', cliente1, 1000.0, 10000.0)
conta2 = Conta('321-4', cliente2, 500.0, 10000.0)
conta3 = Conta('312-4', cliente3, 600.0, 12000.0)

conta1.depositar(250.0)
conta2.depositar(300.0)
conta3.depositar(400.0)
conta1.sacar(100.0)
conta2.sacar(200.0)
conta3.sacar(150.0)
conta1.transferir(conta2, 150.0)
conta1.extrato()
conta2.extrato()
conta3.extrato()

print("\nInformações da Conta 1:")
print("Titular:", conta1.titular)
print("Número:", conta1.numero)
print("Saldo:", conta1.saldo)
print("Total de Contas:", Conta.get_total_de_contas())
print("\nHistórico:")
conta1.historico.imprime()
