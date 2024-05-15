import flet as ft
import numpy as np
import Evaluacion1
def main(page:ft.Page):
    #Diseño de la interfaz
    page.window_width = "1000"
    page.window_height = "700"
    page.window_center()
    page.padding = 40
    page.bgcolor = ft.colors.BLACK
    page.title = "Gauss-Seidel"
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "fonts/OpenSans-Regular.ttf"
    }
    #Funciones
    def validar_entrada(e):
        if(tamMatriz.value.isdigit()):
            True
            page.update()
        else:
            page.dialog = alt1
            alt1.open = True
            page.update()
    def cerrar_alerta(e):
        alt1.open = False
        tamMatriz.value = ""
        page.update()
    def agregar_datos(e):
        #Genero una matriz con random
        matr = [[np.random.randint(1,999) for i in range(int(tamMatriz.value))] for i in range(int(tamMatriz.value))]
        #matr se lo paso Matriz que representa un textField
        matriz.value = str(matr)
        #Busco la ultima colunma y se le asigno a 
        vector.value = matr[-1]
        #Formo una lista
        lista = []
        #Hago un for para que rellene la lista con el numero que se dijo en el tamaño de la matriz
        for i in range(int(tamMatriz.value)):
            lista.append(0)
        vectorX0.value = str(lista)
        #A partir de aqui hago el metodo Gauss seidel
        #A seria mi matriz de numeros
        A = np.array(matr)
        #n seria el contador de filas que tiene la matriz
        n = A.shape[0]
        #B seria los terminos indipendientes o la ultima columna con los ultimos numeros de la fila de la matriz
        b = np.array(matr[-1])
        """X seria mis iteraciones que van a tener mi matriz o el resultado al utilizar el metodo
        Gauss-Seidel"""
        x = np.zeros(int(tamMatriz.value))
        k = 0
        #Imax son las iteraciones
        imax = 100
        cumpl = False
        #Representa la tolerancia de los numeros
        tol = 1e-8
        while(not cumpl and k < imax):
            #hago un vector para colocar los resultados
            xk1 = np.zeros(n)
            for i in range(n):
                #Realizo las operaciones basadas en el metodo-Gauss-Seidel
                s1 = np.dot(A[i,:i],xk1[:i])
                s2 = np.dot(A[i,i+1:],x[i+1:])
                xk1[i] = (b[i]-s1-s2)/A[i,i]
            norma = np.linalg.norm(x-xk1)
            cumpl = norma < tol
            x = xk1
            k+=1
        JtxResultado.value = str(x)
        page.update()
    
    def borrar(e):
        tamMatriz.value = ""
        matriz.value = ""
        vector.value = ""
        vectorX0.value = ""
        JtxResultado.value = ""
        page.update()

    #Titulo
    text1 = ft.Text(
        value = "Metodo Gauss Seidel",
        text_align="CENTER",
        color= ft.colors.WHITE,
        size= 25,
        weight= ft.FontWeight.W_100,
        font_family=  "Kanit"
    )
    page.add(text1)
    textMatriz = ft.Text(
        value= "Datos de la Matriz",
        text_align= "CENTER",
        color= ft.colors.WHITE,
        size= 30,
        weight= ft.FontWeight.W_100,
        font_family=  "Kanit"
    )
    comeM = ft.Text(
        value= "Ingrese el tamaño de la matriz:",
        text_align= "CENTER",
        color= ft.colors.WHITE,
        size= 20,
        weight= ft.FontWeight.W_100,
        font_family=  "Kanit"
    )
    textVector = ft.Text(
        value= "Datos del Vector",
        text_align= "CENTER",
        color= ft.colors.WHITE,
        size= 30,
        weight= ft.FontWeight.W_100,
        font_family=  "Kanit"
    )
    comVectXO = ft.Text(
        value= "Ingrese el vector XO:",
        text_align= "CENTER",
        color= ft.colors.WHITE,
        size= 20,
        weight= ft.FontWeight.W_100,
        font_family=  "Kanit"
    )
    comeResultado = ft.Text(
        value= "Resultado:",
        text_align= "CENTER",
        color= ft.colors.WHITE,
        size= 20,
        weight= ft.FontWeight.W_100,
        font_family=  "Kanit"
    )
    #TextField
    tamMatriz = ft.TextField(
        label= "Tamaño",
        hint_text= "Ingrese el tamaño de la amtriz",
        width= 300,
        border_color= ft.colors.BLACK,
        autofocus= True,
        on_change= validar_entrada
    )
    matriz = ft.TextField(
        label= "Matriz",
        width= 350,
        height= 250,
        multiline= True,
        max_lines= 10,
        min_lines= 10,
        border_color= ft.colors.BLACK,
        color = ft.colors.WHITE,
    )
    vector = ft.TextField(
        label = "Vector",
        border_color= ft.colors.BLACK,
        width= 220,
        color = ft.colors.WHITE,
        multiline= True,

    )
    vectorX0 = ft.TextField(
        label="Vector Inicial",
        hint_text= "Ingrese el vector inicial: ",
        border_color= ft.colors.BLACK,
        width= 220,
    )

    JtxResultado = ft.TextField(
        label= "MGS",
        border_color= ft.colors.BLACK,
        width= 220,
        multiline= True,
        max_lines= 5,
        min_lines= 5
    )

    #Botones

    btnOperaMV = ft.ElevatedButton(
        text= "Operar",
        bgcolor= ft.colors.BLUE,
        color= ft.colors.WHITE,
        width= 100,
        height= 40,
        on_click= agregar_datos
    )
    btnBorrar = ft.ElevatedButton(
        text= "Borrar",
        bgcolor= ft.colors.BLUE,
        color = ft.colors.WHITE,
        width= 100,
        height= 40,
        on_click= borrar
    )
    #Alerta
    alt1 = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Maria por favor es un numero , no una letra"),
        actions=[
            ft.TextButton("Yes", on_click= cerrar_alerta),
            ft.TextButton("No"),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("letra"),
    )
    #Contenedores

    cont1 = ft.Container(
        content= ft.Column(
            [textMatriz,comeM,tamMatriz,matriz],alignment=ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        ),
        padding= 10,
        margin = 10,
        bgcolor= ft.colors.GREEN,
        width= 400,
        height= 450
    )
    cont2 = ft.Container(
        content= ft.Column(
            [textVector,vector,comVectXO,vectorX0,comeResultado,JtxResultado],alignment= ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        ),
        margin = 10,
        padding= 10,
        bgcolor= ft.colors.GREEN,
        width= 400,
        height= 450
    )

    #Filas

    fila1 = ft.Row([cont1,cont2],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment= ft.CrossAxisAlignment.CENTER)
    
    page.add(fila1)

    fila2 = ft.Row([btnOperaMV,btnBorrar],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment=ft.CrossAxisAlignment.END)
    
    page.add(fila2)
    

ft.app(target=main)
