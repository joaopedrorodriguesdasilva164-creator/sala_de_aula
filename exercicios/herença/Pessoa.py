class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

        def apresenatar(self):
            print(f"olá,meu nome é{self.nome} e tenho{self.idade} anos.")

            class Aluno(Pessoa):
                def __init__(self, nome, idade,matricula):
                    super().__init__(nome,idade)
                    self.matricula= matricula
                
                  