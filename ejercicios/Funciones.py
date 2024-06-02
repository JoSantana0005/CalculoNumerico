import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def numerosdecondiciones(matriz):
    n = np.linalg.cond(matriz)
    return n

def NormadeVectoren2d(x1,x2):
    norma = np.linalg.norm(x2-x1)
    print(norma)
    plt.plot([0,norma], label= "Norma")
    plt.title("Norma del vector: {:3f}".format(norma))
    plt.legend()
    plt.show()

def NormaMatricialen2d(x1):
    norma = np.linalg.norm(x1)
    plt.plot([0,norma], label="Norma")
    plt.title("Norma de la matriz:  {:3f}".format(norma))
    plt.legend()
    plt.show()


def NormaVectorialen3d(x1,x2,x0,x3):
    erra = x3-x2-x1
    dist = np.sqrt(erra**2)
    print(dist)
    fig = plt.figure()
    graf = fig.add_subplot(111, projection= "3d")
    [x,y,z] = x0
    graf.scatter(x,y,z, c= "Orange", label= "X0")
    [x,y,z] = x1
    graf.scatter(x,y,z, c= "blue", label= "X1")
    [x,y,z] = x2
    graf.scatter(x,y,z, c= "Green", label= "X2")
    [x,y,z] = x3
    graf.scatter(x,y,z, c= "Green", label= "X2")
    graf.set_xlabel(" Eje x ")
    graf.set_ylabel(" Eje y ")
    graf.set_zlabel(" Eje z ")
    linea = np.concatenate(([x0],[x1]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "X1")
    linea = np.concatenate(([x2],[x1]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "X0")
    linea = np.concatenate(([x0],[x2]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "X2")
    linea = np.concatenate(([x0],[x3]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "X2")
    plt.show()

def NormaMatricialen3d(matriz):
    norma = np.linalg.norm(matriz)
    fig = plt.figure()
    graf = fig.add_subplot(111, projection = "3d")
    [x,y,z] = matriz[:,0,0]
    graf.scatter(x,y,z, c= "Orange", label= "0,0")
    [x,y,z] = matriz[:,0,1]
    graf.scatter(x,y,z, c= "Blue", label= "0,1")
    [x,y,z] = matriz[:,0,2]
    graf.scatter(x,y,z, c= "green", label= "0,2")
    [x,y,z] = matriz[:,1,0]
    graf.scatter(x,y,z, c= "black", label= "1,0")
    [x,y,z] = matriz[:,1,1]
    graf.scatter(x,y,z, c= "brown", label= "1,1")
    [x,y,z] = matriz[:,1,2]
    graf.scatter(x,y,z, c= "gray", label= "1,2")
    [x,y,z] = matriz[:,2,0]
    graf.scatter(x,y,z, c= "pink", label= "2,0")
    [x,y,z] = matriz[:,2,1]
    graf.scatter(x,y,z, c= "violet", label= "2,1")
    [x,y,z] = matriz[:,2,2]
    graf.scatter(x,y,z, c= "violet", label= "2,1")
    linea = np.concatenate(([matriz[:,0,0]],[matriz[:,0,1]]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "matriz[0][0]")
    linea = np.concatenate(([matriz[:,0,1]],[matriz[:,0,2]]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "matriz[0][1]")
    linea = np.concatenate(([matriz[:,0,2]],[matriz[:,1,0]]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "matriz[0][2]")
    linea = np.concatenate(([matriz[:,1,0]],[matriz[:,1,1]]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "matriz[1][0]")
    linea = np.concatenate(([matriz[:,1,1]],[matriz[:,1,2]]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "matriz[1][1]")
    linea = np.concatenate(([matriz[:,1,2]],[matriz[:,2,0]]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "matriz[1][2]")
    linea = np.concatenate(([matriz[:,2,0]],[matriz[:,2,1]]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "matriz[2][0]")
    linea = np.concatenate(([matriz[:,2,1]],[matriz[:,2,2]]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    graf.plot(x,y,z, label= "matriz[2][1]")
    graf.set_xlabel("Eje X")
    graf.set_ylabel("Eje Y")
    graf.set_zlabel("Eje z")
    plt.show()
