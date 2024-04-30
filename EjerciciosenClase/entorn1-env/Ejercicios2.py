class Cancion:
    # Constructor
    def __init__(self,titulo = str,artista = str,durac = int):
        self.titulo = titulo
        self.artista = artista
        self.durac = durac
    # Getters

    def getTitulo(self):
        return self.titulo
    def getArtista(self):
        return self.artista
    def getDurac(self):
        return self.durac
    
    # Setters

    def setTitulo(self,titulo):
        self.titulo = titulo
    def setArtista(self,artista):
        self.artista = artista
    def setDurac(self,durac):
        self.durac = durac
    
    # Funciones

    def reproducir(self):
        print("se esta reproduciendo la cancion: ",self.titulo, " Del artista: ",self.artista)

    def pausar(self):
        cont = 0
        pausa = int(input("Ingrese el momento quiere parar la cancion:  "))
        for i in range(self.durac):
            cont += 1
            if(cont == pausa):
                print("Se pauso la cancion en el momento ", cont)
        if(pausa == self.durac):
            print("Se termino la cancion", cont)
                    


canc1 = Cancion("MAI","milo j",324)    
canc1.reproducir()
canc1.pausar()  