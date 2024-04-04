class main:
    pass
print("testando o projeto")

from cliente import cliente

from Conta import Conta

c1= cliente("joão", "114444-2222")
conta=Conta(c1.nome,6565,0)

print(conta.titular, "numero: ", conta.numero, "seu saldo: ", conta.saldo)
