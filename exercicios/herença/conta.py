class conta:
    def __init__(self,titular,saldo):
        self.titular= titular
        self.saldo=saldo
        
        class contapoupanca(conta):
            def render_juros(self,taxa):
                self.saldo+=self.saldo*(taxa/100)
                
        