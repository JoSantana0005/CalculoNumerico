import CalculoNumerico.ejercicios.Funciones as Funciones
import numpy as np
#Programa principal

matriz = np.array([[2,3,4],[1,4,56],[4,7,8]])
result = Funciones.numerosdecondiciones(matriz)
print("Numeros de condiciones: " + str(result))
