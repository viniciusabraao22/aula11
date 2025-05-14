class Forma:
    def __init__(self):
        self.area=0
        self.perimetro=0


class retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculaArea(self,base,altura):
        self.Area=base*altura
        print(f"a area do retangulo e {self.Area}")
    def calculaArea(self,base,altura):
        self.Area = (base * altura) * 2
        print(f"a area do retangulo e {self.perimetro}")

class Triangulo(Forma):
    def __init__(self,base, altura):
        super().__init__()
        self.base=base
        self.altura=altura
    def calculaArea(self):
        self.Area=(self.base*self.altura)/2
        print(self.area)
    def calculaPerimetro(self):
        self.perimentro=self.base
        print(self.perimentro)
