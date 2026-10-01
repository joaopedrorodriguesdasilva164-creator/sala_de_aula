class veiculo:
    def __init__(self,marca,modelo):
       self.marca=marca
       self.modelo=modelo

       class moto(veiculo):
                 def __init__(self,marca,modelo,cilindradas):
                     super().__init__(marca,modelo)
                     self.cilindradas=cilindradas
           
