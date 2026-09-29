class Pessoa:
    
    nome:str
    ciade:str
    def __init__ ( self, nome, cidade ):
        self.nome=nome
        self.cidade= cidade

    
    def apresentar(self):
        return f"olá, meu nome é self. self.cidade"