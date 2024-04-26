#Crear una clase llamada persona con los atributos(nombre,edad,dni)
#que tenga un contructor vacio , validar la entrada de datos que muestre los getters y setters
#mostrar los datos de la persona por consola y hacer una funcion que devuelva un boolean si es mayor de edad

class persona:
    #Contructor
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    #Getters
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_dni(self):
        return self.dni
    #Setters
    def set_nombre(self,nombre:str):
        self.nombre = nombre
    def set_edad(self,edad:int):
        self.edad = edad
    def set_dni(self,dni:str):
        self.dni = dni
    #Funciones
    def mayordeedad(self):
        if(self.edad > 18):
            return True
        else:
            return False
    def mostrarDatos(self):
        print("Nombre          edad         dni ")
        print("{0:<10}   {1:^10d}  {2:^10}".format(self.nombre,self.edad,self.dni))

nombre = input("Ingrese un nombre: ")
edad = int(input("Ingrese la edad de la persona: "))
dni = input("Ingrese la cedula de la persona: ")
if(len(dni) == 8 and nombre.isalpha() == True):
    nuevo = persona(nombre,edad,dni)
    nuevo.mostrarDatos()
    result = nuevo.mayordeedad()
    print("¿La persona es mayor?" + " : "  + str(result))
else:
    print("Se equivoco colocando un dato")
   
