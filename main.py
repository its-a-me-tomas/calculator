# invocar a los archivos para los métodos
from seidel import *
from secante import *
#librerias para la interfaz grafica (aun trabajando)
from tkinter import *
"""
#Opciones para la calculadora *consola*
inp = int(input("solución de sistema de ecuaciones(2) o raiz de ecuación no lineal(1)->"))
#raiz de ecuaciones no lineales secante#
if inp == 1:
    fun = input("Ingresa la función-->")
    a = float(input("1er Aproximación Inicial ->"))
    b = float((input("2da Aproximación Inicial ->")))
    ea = float((input("Error permitido ->")))
    secante(fun, a, b, ea)
#seidel Sistemas de ecuaciones #-7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6 || -10;35;3;-6
elif inp == 2 :
    a = converA(input("Ingrese la matriz de coeficientes->"))
    b = converB(input("Ingresa el vector de términos independientes->"))
    e = float(input("Error permitido->"))
    maxI = int(input("Máxima de iteraciones->"))
    seidel(a,b,e,maxI)
"""

############INTERFAZ GRAFICA#########################
#INICIALIZAR#
root = Tk()
root.withdraw()
backg = PhotoImage(file = "img/back1.png")
current_window  = None

####   windows   ####
def windowsys(): #sistema de ecuaciones#
    global current_window
    if current_window is not None:
        current_window.destroy()
    current_window = Toplevel(root)
    current_window.wm_protocol("WM_DELETE_WINDOW", mainWindow)
    window = current_window
    #properties
    window.iconbitmap('img/Calculator.ico')
    window.title('Calculadora de Sistemas de ecuaciones no lineales')
    window.resizable(0,0)
    window.geometry("720x420")
    #extra settings
    window.config(cursor="pirate")
    #mensaje
    asd = Label(window, text="¡Hola,Bienvenido a la Calculadora de sistema de ecuaciones y sistemas no lineales!")
    asd.place(x=130, y=50, width=450, height=20)
    #entrada de datos
    matrix = Entry(window, width=50)
    matrix.place(x=130, y=200, width=50)
    independiente = Entry(window, width=50)
    independiente.place(x=130, y=230, width=50)
    error = Entry(window, width=50)
    error.place(x=130, y=260, width=50)
    Iteraciones = Entry(window, width=50)
    Iteraciones.place(x=130, y=290, width=50)
    #llamada a function#
    
    #ventana de secante o sistema
    window.mainloop()

def windowequ():  #ecuaciones no lineales#
    global current_window
    if current_window is not None:
        current_window.destroy()
    current_window = Toplevel(root)
    current_window.wm_protocol("WM_DELETE_WINDOW", mainWindow)
    window = current_window
    window.iconbitmap('img/Calculator.ico')
    window.title('Calculadora de sistemas de ecuaciones')
    window.resizable(0,0)
    window.geometry("720x420")
    #extra settings
    window.config(cursor="pirate")
    #mensaje
    asd = Label(window, text="¡Hola,Bienvenido a la Calculadora de sistema de ecuaciones!")
    asd.place(x=130, y=50, width=450, height=20)
    #entrada de datos
    function = Entry(window, width=50)
    function.place(x=130, y=200, width=50)
    intervaloA = Entry(window, width=50)
    intervaloA.place(x=130, y=230, width=50)
    intervaloB = Entry(window, width=50)
    intervaloB.place(x=130, y=260, width=50)
    Error = Entry(window, width=50)
    Error.place(x=130, y=290, width=50)
    #llamada a function#

    ##
    window.mainloop()

def mainWindow():
    global current_window, backg
    if current_window is not None:
        current_window.destroy()
    current_window = Toplevel(root)
    current_window.wm_protocol("WM_DELETE_WINDOW", root.destroy)
    window = current_window #crea ventana    
    window.iconbitmap('img/Calculator.ico')
    window.title('Calculadora')
    window.resizable(0,0)
    window.geometry("260x320")
    #extra settings
    window.config(cursor="pirate")
    #image background
    canva = Canvas(window, width = 260, height = 320)
    canva.pack(fill = 'both', expand = True)
    canva.create_image(0,0, image = backg, anchor = 'nw')
    #botones para elegir
    pto = Button(window, text="Calculadora \n Sistema de ecuaciones", command=windowsys, font = 'Corbel -15')
    pto2 = Button(window, text="Calculadora \n Ecuaciones no lineales", command=windowequ, font = 'Corbel -15')
    pto.place(x=55, y=145)
    pto2.place(x=55, y=215)
    #mensaje
    asd = Label(window, text = "Bienvenido!", font = 'Corbel -35 bold')
    asd.place(x=35, y=35, width=200, height=60)
    #ventana de secante o sistema
    window.mainloop()

window = mainWindow()
