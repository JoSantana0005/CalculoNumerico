import Funciones
import numpy as np
import random
#Programa principal
i = 1
while(i < 5):
    condi = random.randint(1,5)
    if(condi == 1):
        ma = np.array([[3,4,5,7],[3,4,6,8]])
        result = Funciones.numerosdecondiciones(ma)
        print("El numero de condiciones de la matriz es: " + str(result))
    elif(condi == 2):
        arr1 = np.array([30,40,60,80])
        arr2 = np.array([10,20,30,40])
        Funciones.NormadeVectoren2d(arr1,arr2)
    elif(condi == 3):
        matri = np.array([[3,2],[4,10],[4,11]])
        Funciones.NormaMatricialen2d(matri)
    elif(condi == 4):
        x0 = np.array([35,62,10])
        x1 = np.array(3,56,10)
        x2 = np.array([10,5,70])
        x3 = np.array([23,45,86])
        Funciones.NormaVectorialen3d(x1,x2,x0,x3)
    else:
        mat= np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
        Funciones.NormaMatricialen3d(mat)
    i += 1

