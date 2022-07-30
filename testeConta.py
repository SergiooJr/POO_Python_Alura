from conta import Conta
conta = Conta(123, "Nico", 55.0, 1000.0) # "conta" é uma referência que armazena o local na memória onde está armazenado o objeto
conta2 = Conta(321, "Marco", 100.0, 1000.0) 
#                      IMPRIMINDO OS ATRIBUTOS
print(conta.saldo) # objeto.atributo