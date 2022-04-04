class Quadrado:


    def __init__(self, lado):
        self.lado = lado
        self.__area = lado**2


    def retorna_area(self):
        print(self.__area)


quadrado = Quadrado(4)
quadrado.retorna_area()
quadrado.area = 7
quadrado.retorna_area()
print(quadrado.__dict__)
quadrado._Quadrado__area = 13
quadrado.retorna_area()