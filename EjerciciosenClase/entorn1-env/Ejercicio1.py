
class FiguraGeometrica:
    #Constructor
    def __init__(self,nombre = str,nLado = int):
        self.nombre = nombre
        self.nLado = nLado
    
    #Getters
    
    def getNombre(self):
        return self.nombre
    def getNlado(self):
        return self.nLado
    
    #Setters
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setNlado(self,nLado):
        self.nLado = nLado
    
    #Funciones

    def Calculo_area(self):
        if(self.nombre.lower() == "cuadrado" and self.nLado == 4):
            return (self.nLado)**2
        elif(self.nombre.lower() == "triangulo" and self.nLado == 3):
            altura = 2*self.nLado
            return self.nLado*altura / 2
        elif(self.nombre.lower() == "rectangulo" and self.nLado == 4):
            return self.nLado*self.nLado
    def calculo_peri(self):
        if(self.nombre.lower() == "cuadrado" and self.nLado == 4):
            return 4*self.nLado
        elif(self.nombre.lower() == "triangulo" and self.nLado == 3):
            return 3*self.nLado
        elif(self.nombre.lower() == "rectangulo" and self.nLado == 4):
            return 2*self.nLado + 2*self.nLado

# Principal

nom = input("Ingrese la figura geometrica: ")
lado = int(input("Ingrese los lados que tien la figura: "))

fig1 = FiguraGeometrica(nom,lado)

resultA = fig1.Calculo_area()
print("El area de la figura es: " + str(resultA))
resultP = fig1.calculo_peri()
print("El perimetro de la figura es: " + str(resultP))