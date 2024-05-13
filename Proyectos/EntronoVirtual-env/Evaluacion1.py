import flet as ft
import ParteII
def main(page:ft.Page):
    #Diseño de la pagina
    page.window_width = "500"
    page.window_height = "670"
    page.window_center()
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = "CENTER"
    page.title = "Convertidor"
    page.padding = 70
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "fonts/OpenSans-Regular.ttf"
    }
    #Funciones

    
    
    def agregar_datos(e: ft.KeyboardEvent):
        jtx1.value = jtx1.value + e.control.text
        page.update()
    
    def condi_Drop2(e):
        """Conversiones para todos los sistemas numericos
            En algunos casos me ayudaba con algunas conversiones
            como de ternario a cuatenario"""
        if(Drop1.value == "Decimal" and Drop2.value == "Bin"):
            jtx2.value = bin(int(jtx1.value))[2::]
            page.update()
        elif(Drop1.value == "Decimal" and Drop2.value == "Octa"):
            jtx2.value = oct(int(jtx1.value))[2::]
            page.update()
        elif(Drop1.value == "Decimal" and Drop2.value == "Hexa"):
            jtx2.value = hex(int(jtx1.value))[2::]
            page.update()
        elif(Drop1.value == "Bin" and Drop2.value == "Decimal"):
            entrada = jtx1.value
            pos = len(entrada)
            deci = 0
            for i in reversed(entrada):
                if i == "1":
                    deci = deci + pow(2,(len(entrada) - pos))
                pos = pos - 1
            jtx2.value = str(deci)
            page.update()
        elif(Drop1.value == "Bin" and Drop2.value == "Octa"):
            entrada = jtx1.value
            pos = len(entrada)
            deci = 0
            for i in reversed(entrada):
                if i == "1":
                    deci = deci + pow(2,(len(entrada) - pos))
                pos = pos - 1
            binaaDeci = str(deci)
            jtx2.value = oct(int(binaaDeci))[2::]
            page.update()
        elif(Drop1.value == "Bin" and Drop2.value == "Hexa"):
            entrada = jtx1.value
            pos = len(entrada)
            deci = 0
            for i in reversed(entrada):
                if i == "1":
                    deci = deci + pow(2,(len(entrada) - pos))
                pos = pos - 1
            binaaDeci = str(deci)
            jtx2.value = hex(int(binaaDeci))[2::]
            page.update()
        elif(Drop1.value == "Octa" and Drop2.value == "Decimal"):
            jtx2.value = str(int(jtx1.value,8))
            page.update()
        elif(Drop1.value == "Octa" and Drop2.value == "Bin"):
            octaadecimal = str(int(jtx1.value,8))
            jtx2.value = bin(int(octaadecimal))[2::]
            page.update()
        elif(Drop1.value == "Octa" and Drop2.value == "Hexa"):
            octaadecimal = str(int(jtx1.value,8))
            jtx2.value = hex(int(octaadecimal))[2::]
            page.update()
        elif(Drop1.value == "Hexa" and Drop2.value == "Decimal"):
            jtx2.value = str(int(jtx1.value,16))
            page.update()
        elif(Drop1.value == "Hexa" and Drop2.value == "Bin"):
            hexaaDecimal = str(int(jtx1.value,16))
            jtx2.value = bin(int(hexaaDecimal))[2::]
            page.update()
        elif(Drop1.value == "Hexa" and Drop2.value == "Octa"):
            hexaaDecimal = str(int(jtx1.value,16))
            jtx2.value = oct(int(hexaaDecimal))[2::]
            page.update()
        
        elif(Drop1.value == "Decimal" and Drop2.value == "Ternario"):
            n = int(jtx1.value)
            if n == 0:
                jtx2.value = '0'
                page.update()
                return
            nums = []
            while n:
                n, r = divmod(n, 3)
                nums.append(str(r))
            jtx2.value = ''.join(reversed(nums))
            page.update()
        elif(Drop1.value == "Bin" and Drop2.value == "Ternario"):
            entrada = jtx1.value
            pos = len(entrada)
            deci = 0
            for i in reversed(entrada):
                if i == "1":
                    deci = deci + pow(2,(len(entrada) - pos))
                pos = pos - 1
            binaaDeci = deci
            if binaaDeci == 0:
                jtx2.value = '0'
                page.update()
                return
            nums = []
            while binaaDeci:
                binaaDeci, r = divmod(binaaDeci, 3)
                nums.append(str(r))
            jtx2.value = ''.join(reversed(nums))
            page.update()
        elif(Drop1.value == "Octa" and Drop2.value == "Ternario"):
            octaadecimal = int(jtx1.value,8)
            if octaadecimal == 0:
                jtx2.value = '0'
                page.update()
                return
            nums = []
            while octaadecimal:
                octaadecimal, r = divmod(octaadecimal, 3)
                nums.append(str(r))
            jtx2.value = ''.join(reversed(nums))
            page.update()
        elif(Drop1.value == "Hexa" and Drop2.value == "Ternario"):
            hexaaDecimal = int(jtx1.value,16)
            if hexaaDecimal == 0:
                jtx2.value = '0'
                page.update()
                return
            nums = []
            while hexaaDecimal:
                hexaaDecimal, r = divmod(hexaaDecimal, 3)
                nums.append(str(r))
            jtx2.value = ''.join(reversed(nums))
            page.update()
        elif(Drop1.value == "Decimal" and Drop2.value == "Cuatenario"):
            n = int(jtx1.value)
            if n == 0:
                jtx2.value = "0"
                page.update()
                return
            cuart = ""
            while n > 0:
                cuart = str(n % 4) + cuart
                n //= 4
            jtx2.value = cuart
            page.update()
        elif(Drop1.value == "Bin" and Drop2.value == "Cuatenario"):
            entrada = jtx1.value
            pos = len(entrada)
            deci = 0
            for i in reversed(entrada):
                if i == "1":
                    deci = deci + pow(2,(len(entrada) - pos))
                pos = pos - 1
            binaaDeci = deci

            if(binaaDeci == 0):
                jtx2.value = "0"
                page.update()
                return
            cuart = ""
            while binaaDeci > 0:
                cuart = str(binaaDeci%4) + cuart
                binaaDeci//=4
            jtx2.value = cuart
            page.update()
        elif(Drop1.value == "Octa" and Drop2.value == "Cuatenario"):
            octaadecimal = int(jtx1.value,8)
            if(octaadecimal == 0):
                jtx2.value = "0"
                page.update()
                return
            cuart = ""
            while octaadecimal > 0:
                cuart = str(octaadecimal%4) + cuart
                octaadecimal//=4
            jtx2.value = cuart
            page.update()
        elif(Drop1.value == "Hexa" and Drop2.value == "Cuatenario"):
            hexaaDecimal = int(jtx1.value,16)
            if(hexaaDecimal == 0):
                jtx2.value = "0"
                page.update()
                return
            cuart = ""
            while hexaaDecimal > 0:
                cuart = str(hexaaDecimal%4) + cuart
                hexaaDecimal//=4
            jtx2.value = cuart
            page.update()
        elif(Drop1.value == "Ternario" and Drop2.value == "Decimal"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(3**pos)
                pos -= 1
            jtx2.value = str(deci)
            page.update()
        elif(Drop1.value == "Ternario" and Drop2.value == "Bin"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(3**pos)
                pos -= 1
            ternaDeci = deci
            jtx2.value = bin(int(ternaDeci))[2::]
            page.update()
        elif(Drop1.value == "Ternario" and Drop2.value == "Octa"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(3**pos)
                pos -= 1
            ternaDeci = deci
            jtx2.value = oct(int(ternaDeci))[2::]
            page.update()
        elif(Drop1.value == "Ternario" and Drop2.value == "Hexa"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(3**pos)
                pos -= 1
            ternaDeci = deci
            jtx2.value = hex(int(ternaDeci))[2::]
            page.update()
        elif(Drop1.value == "Cuatenario" and Drop2.value == "Decimal"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(4**pos)
                pos -= 1
            jtx2.value = str(deci)
            page.update()
        elif(Drop1.value == "Cuatenario" and Drop2.value == "Bin"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(4**pos)
                pos -= 1
            CuaraDeci = deci
            jtx2.value = bin(int(CuaraDeci))[2::]
            page.update()
        elif(Drop1.value == "Cuatenario" and Drop2.value == "Octa"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(4**pos)
                pos -= 1
            CuaraDeci = deci
            jtx2.value = oct(int(CuaraDeci))[2::]
            page.update()
        elif(Drop1.value == "Cuatenario" and Drop2.value == "Hexa"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(4**pos)
                pos -= 1
            CuaraDeci = deci
            jtx2.value = hex(int(CuaraDeci))[2::]
            page.update()
        elif(Drop1.value == "Cuatenario" and Drop2.value == "Ternario"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(4**pos)
                pos -= 1
            CuaraDeci = deci

            if CuaraDeci == 0:
                jtx2.value = '0'
                page.update()
                return
            nums = []
            while CuaraDeci:
                CuaraDeci, r = divmod(CuaraDeci, 3)
                nums.append(str(r))
            jtx2.value = ''.join(reversed(nums))
            page.update()

        elif(Drop1.value == "Ternario" and  Drop2.value == "Cuatenario"):
            condi = jtx1.value
            if(condi == "0"):
                jtx2.value = "0"
                page.update()
                return
            deci = 0
            pos = len(condi) - 1
            for digito in condi:
                val = int(digito)
                deci += val*(3**pos)
                pos -= 1
            ternaDeci = deci

            if ternaDeci == 0:
                jtx2.value = "0"
                page.update()
                return
            cuart = ""
            while ternaDeci > 0:
                cuart = str(ternaDeci % 4) + cuart
                ternaDeci //= 4
            jtx2.value = cuart
            page.update()

    """Esta funcion hace que los botones se han accesible o no
        dependiendo del sistema numerico"""
    def condi_drop1(e):
        btn1.disabled = False
        btn2.disabled = False
        btn3.disabled = False
        btn4.disabled = False
        btn5.disabled = False
        btn6.disabled = False
        btn7.disabled = False
        btn8.disabled = False
        btn9.disabled = False
        btnA.disabled = False
        btnB.disabled = False
        btnC.disabled = False
        btnD.disabled = False
        btnE.disabled = False
        btnF.disabled = False
        page.update()
        if(Drop1.value == "Bin"):
            btn2.disabled = True
            btn3.disabled = True
            btn4.disabled = True
            btn5.disabled = True
            btn6.disabled = True
            btn7.disabled = True
            btn8.disabled = True
            btn9.disabled = True
            btnA.disabled = True
            btnB.disabled = True
            btnC.disabled = True
            btnD.disabled = True
            btnE.disabled = True
            btnF.disabled = True
            page.update()
        elif(Drop1.value == "Octa"):
            btn8.disabled = True
            btn9.disabled = True
            btnA.disabled = True
            btnB.disabled = True
            btnC.disabled = True
            btnD.disabled = True
            btnE.disabled = True
            btnF.disabled = True
            page.update()
        elif(Drop1.value == "Ternario"):
            btnA.disabled = True
            btnB.disabled = True
            btnC.disabled = True
            btnD.disabled = True
            btnE.disabled = True
            btnF.disabled = True
            page.update()
        elif(Drop1.value == "Cuatenario"):
            btnA.disabled = True
            btnB.disabled = True
            btnC.disabled = True
            btnD.disabled = True
            btnE.disabled = True
            btnF.disabled = True
            page.update()
        elif(Drop1.value == "Decimal"):
            btnF.disabled = True
            btnE.disabled = True
            btnD.disabled = True
            btnC.disabled = True
            btnB.disabled = True
            btnA.disabled = True
            page.update()
        else:
            btn1.disabled = False
            btn2.disabled = False
            btn3.disabled = False
            btn4.disabled = False
            btn5.disabled = False
            btn6.disabled = False
            btn7.disabled = False
            btn8.disabled = False
            btn9.disabled = False
            btnA.disabled = False
            btnB.disabled = False
            btnC.disabled = False
            btnD.disabled = False
            btnE.disabled = False
            btnF.disabled = False
            page.update()

    #Funcion que borrar Todo lo que se haya puesto en los textField y Dropdown
    def BorrarTodo(e):
        jtx1.value = ""
        jtx2.value = ""
        Drop1.value = ""
        Drop2.value = ""
        page.update()
    #Funcion que borrar un caracter en el textField de entrada
    def borrar(e: ft.KeyboardEvent):
        jtx1.value = jtx1.value[:-1]
        page.update()

    
    #Titulo
    text1 = ft.Text(
        value= "Convertidor de Sistemas Numericos",
        weight= ft.FontWeight.W_100,
        size= 25,
        color= ft.colors.WHITE,
        text_align= "CENTER",
        font_family= "Kanit"
    )
    page.add(text1)

    text2 = ft.Text(
        value= "Ingrese el numero que quiere convertir: ",
        size = 15,
        color= ft.colors.WHITE,
        text_align= "CENTER",
        weight= ft.FontWeight.W_100,
        font_family= "Kanit"

    )
    page.add(text2)
    #Drop y TextField
    Drop1 = ft.Dropdown(
        hint_text= "Elige un sistema",
        width= 180,
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Bin"),
            ft.dropdown.Option("Octa"),
            ft.dropdown.Option("Hexa"),
            ft.dropdown.Option("Ternario"),
            ft.dropdown.Option("Cuatenario"),
            ],
        autofocus= True,
        border_color= ft.colors.BLUE,
        color= ft.colors.WHITE,
        on_change = condi_drop1
    )

    jtx1 = ft.TextField(
        label= "0",
        width= 160,
        color= ft.colors.WHITE,
        border_color= ft.colors.BLUE,
        multiline= True,
        disabled= True,
    )

    Drop2 = ft.Dropdown(
        hint_text= "Elige un sistema",
        width= 180,
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Bin"),
            ft.dropdown.Option("Octa"),
            ft.dropdown.Option("Hexa"),
            ft.dropdown.Option("Ternario"),
            ft.dropdown.Option("Cuatenario"),
            ],
        autofocus= True,
        border_color= ft.colors.BLUE,
        color= ft.colors.WHITE,
        on_change= condi_Drop2
    )

    jtx2 = ft.TextField(
        label= "Salida",
        width= 160,
        color= ft.colors.WHITE,
        multiline= True,
        border_color= ft.colors.BLUE,
    )

    #Botones

    btnAC = ft.ElevatedButton(
        text= "AC",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= BorrarTodo
    )
    btnX = ft.ElevatedButton(
        text= "X",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= borrar
    )

    btnF = ft.ElevatedButton(
        text= "F",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btnE = ft.ElevatedButton(
        text= "E",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn7 = ft.ElevatedButton(
        text= "7",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn8 = ft.ElevatedButton(
        text= "8",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn9 = ft.ElevatedButton(
        text= "9",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btnD = ft.ElevatedButton(
        text= "D",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn4 = ft.ElevatedButton(
        text= "4",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn5 = ft.ElevatedButton(
        text= "5",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn6 = ft.ElevatedButton(
        text= "6",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btnC = ft.ElevatedButton(
        text= "C",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn1 = ft.ElevatedButton(
        text= "1",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn2 = ft.ElevatedButton(
        text= "2",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn3 = ft.ElevatedButton(
        text= "3",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btnB = ft.ElevatedButton(
        text= "B",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btn0 = ft.ElevatedButton(
        text= "0",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    btnA = ft.ElevatedButton(
        text= "A",
        width= 70,
        height= 40,
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        on_click= agregar_datos
    )
    #Filas de la interfaz
    fila1 = ft.Row(controls=[Drop1,jtx1],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment= ft.CrossAxisAlignment.CENTER)
    
    page.add(fila1)
    
    fila2 = ft.Row(controls=[Drop2,jtx2],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment= ft.CrossAxisAlignment.CENTER)
    
    page.add(fila2)

    fila3 = ft.Row(controls=[btnAC,btnX,btnF,btnE],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(fila3)

    fila4 = ft.Row(controls=[btn7,btn8,btn9,btnD],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(fila4)

    fila5 = ft.Row(controls=[btn4,btn5,btn6,btnC],alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(fila5)

    fila6 = ft.Row(controls= [btn1,btn2,btn3,btnB],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(fila6)

    fila7 = ft.Row(controls=[btn0,btnA],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER)

    page.add(fila7)
    page.update()

ft.app(target= main)
