# antes de criarmos um objeto, preciamos criar classes(caracteristicas)
class Conta:
    # construindo o objeto
    # self é a referência que sabe onde encontrar o objeto
    def __init__(self, numero, titular, saldo, limite): # função construtura
        print(f"Contruindo objeto...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite