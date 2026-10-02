class forma:
    def area(self):
        return 0
    class quadrado(forma):
        def __init__(self,lado):
           self.lado=lado
        def area(self):
                return self.lado*self.lado
