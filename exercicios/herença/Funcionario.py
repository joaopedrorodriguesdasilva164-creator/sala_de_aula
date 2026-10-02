class funcionario:
    def __init__(self, nome, salario):
        self.nome=nome
        self.salario=salario

class Gerente(funcionario):
            def autorizar_pagmamento(self):
                print(f"o gerente{self.nome}autorizou o pagamento.")
