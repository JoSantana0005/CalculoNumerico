#Programa que realiza el Teorema de Pitagoras

catetoa <- as.numeric(readline("Introduzca el cateto a: "))
catetob <- as.numeric(readline("Introduzca el cateto b: "))
catetoa
catetob
hipo = sqrt((catetoa)**2 + (catetob)**2)
hipo
print("La hipotenusa es de: " + hipo)