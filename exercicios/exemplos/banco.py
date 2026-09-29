class ContaBancaria:

    def __init__(self, titular, saldo):
        self.tiular=titular
        self.saldo = 0 if saldo == None else saldo

        def depositar(self, valor):
            self.saldo+= valor
