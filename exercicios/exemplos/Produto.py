class produto:
    def __init__ (self, nome, preco):
        self.nome=nome
        self.preco=preco

    def aplicar_desconto( self, percentual):
        self.preco-=self.preco*(percentual/100)