from teste import *
conta = cria_conta(123, "Nico", 55.0, 1000.0)
deposita(conta, 300.0)
extrato(conta)
saca(conta, 100.0)
extrato(conta)

# podemos fazer isso para alterar o saldo:
conta["saldo"] = -300.0
extrato(conta)
# deveriamos manipular o saldo da conta utilizando apenas as funções

 