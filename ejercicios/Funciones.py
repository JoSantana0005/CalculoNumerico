import numpy as np
import matplotlib.pyplot as plt
def numerosdecondiciones(matriz):
    n = np.linalg.cond(matriz)
    return n

def NormadeVector(x1,x2):
    norma = np.linalg.norm(x2-x1)
    print(norma)
    plt.plot([0,norma], label= "Norma")
    plt.legend()
    plt.show()


