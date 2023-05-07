class Ventana:
    
    def __init__(self, titulo, xi=0, yi=0, xd=100, yd=100):
        self.__titulo = titulo
        self.__xi = max(xi, 0)
        self.__yi = max(yi, 0)
        self.__xd = min(xd, 500)
        self.__yd = min(yd, 500)
    
    def mostrar(self):
        print(f"Ventana '{self.__titulo}': ({self.__xi}, {self.__yi}), ({self.__xd}, {self.__yd})")
        
    def ancho(self):
        return self.__xd - self.__xi
    
    def alto(self):
        return self.__yd - self.__yi
        
    def moverDerecha(self, unidades=1):
        self.__xi = min(self.__xi + unidades, 500 - self.ancho())
        self.__xd = self.__xi + self.ancho()
        
    def moverIzquierda(self, unidades=1):
        self.__xi = max(self.__xi - unidades, 0)
        self.__xd = self.__xi + self.ancho()
        
    def subir(self, unidades=1):
        self.__yi = max(self.__yi - unidades, 0)
        self.__yd = self.__yi + self.alto()
        
    def bajar(self, unidades=1):
        self.__yi = min(self.__yi + unidades, 500 - self.alto())
        self.__yd = self.__yi + self.alto()
        
    def getTitulo(self):
        return self.__titulo