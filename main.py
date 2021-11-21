# invocar a los archivos para los métodos
from seidel import *
from secante import *
#librerias para la interfaz grafica (aun trabajando)
from tkinter import *
from tkinter.ttk import *
"""
#-7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6 || -10;35;3;-36 ejemplo de entrada
#options for calculator *consola*
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
############
# INTERFAZ GRAFICA
############
#INICIALIZAR#
root = Tk()
root.withdraw()
root.wm_attributes('-transparentcolor','#979191')
#style configure
style = Style()
style.theme_use(themename='clam')
style.configure('TButton', font=('Candara', -12))
style.configure('TButton', justify='center')
style.configure('TLabel', font=('Candara',-13))
style.configure('TLabel',background = '#979191')
#global var
backg, back2 = PhotoImage(file = "img/back1.png"), PhotoImage(file = "img/back2.png")
current_window, result =  None, StringVar()
####
# windows 
#####

def windowsys(): #sistema de ecuaciones#
    global current_window, back2, result
    result.set('')
    if current_window is not None:
        current_window.destroy()
    current_window = Toplevel(root)
    current_window.wm_protocol("WM_DELETE_WINDOW", mainWindow)
    window = current_window
    #properties
    window.iconbitmap('img/Calculator.ico')
    window.title('Calculadora')
    window.resizable(0,0)
    window.geometry("720x420")
    #image background
    canva = Canvas(window, width = 720, height = 420)
    canva.pack(fill = 'both', expand = True)
    canva.create_image(0,0, image = back2, anchor = 'nw')
    #extra settings
    window.config(cursor="circle")
    #mensaje
    asd = Label(window,
                text="Calculadora de sistemas de ecuaciones por el método Gauss-Seidel",
                font="Candara -20 bold")
    asd.place(x=80, y=20)

    #entrada de datos
    mat = Label(window, 
                text="Matrix de Coeficientes del sistema\nEjemplo: -7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6",
                justify='center')
    matrix = Entry(window, width=40)
    mat.place(x=47,y=80)
    matrix.place(x=40, y=115)
    
    ind = Label(window,
                text = 'Términos independientes\nEjemplo: -10;35;3;-6',
                justify='center')
    independiente = Entry(window)
    ind.place(x=75,y=140)
    independiente.place(x=85, y=175)
    
    er = Label(window,
                text = 'Error permitido\nEjemplo: 0.001',
                justify='center')
    error = Entry(window)
    er.place(x=100,y=200)
    error.place(x=85, y=235)
    
    ite = Label(window,
                text='Numero de iteraciones\nEjemplo: 20',
                justify ='center')
    Iteraciones = Entry(window)
    ite.place(x=83,y=260)
    Iteraciones.place(x=85, y=295)
    
    impresion = Label(window,textvariable=result,background = '#979191')
    #get data# #llamada a function#
    active = Button(window,
        text="Calcular raiz",
        command = lambda: result.set(siedel(converA(matrix.get()), converB(independiente.get()), float(error.get()), int(Iteraciones.get()))))
    active.place(x=95,y=330)
    impresion.place(x=370 ,y= 70)
    #mainloop#
    window.mainloop()

def windowequ():  #ecuaciones no lineales#
    global current_window, back2, result
    result.set("")
    if current_window is not None:
        current_window.destroy()
    current_window = Toplevel(root)
    current_window.wm_protocol("WM_DELETE_WINDOW", mainWindow)
    window = current_window
    window.iconbitmap('img/Calculator.ico')
    window.title('Calculadora')
    window.resizable(0,0)
    window.geometry("720x420")
    #image background#
    canva = Canvas(window, width = 720, height = 420)
    canva.pack(fill = 'both', expand = True)
    canva.create_image(0,0, image = back2, anchor = 'nw')
    #extra settings
    window.config(cursor="circle")
    #mensaje
    asd = Label(window,
                text="Calculadora de raices de ecuaciones no lineales\npor el método de la secante",
                font=('Candara -20 bold'),
                justify='center')
    asd.place(x=160, y=10)

    #entrada de datos
    fun = Label(window, 
            text="Función a evaluar\nEjemplo: 4*x**3+2",
            justify='center')
    function = Entry(window,
                    width=40)
    fun.place(x=95,y=80)
    function.place(x=35, y=115)
    
    intA= Label(window,
                text = '1er Aproximación',
                justify='center')
    intervaloA = Entry(window,
                        width=10)
    intA.place(x=40,y=150)
    intervaloA.place(x=60, y=180)
    
    intB = Label(window,
                text = '2da Aproximación',
                justify='center')
    intervaloB = Entry(window,
                        width=10)
    intB.place(x=165,y=150)
    intervaloB.place(x=185, y=180)
    
    err = Label(window,
                text='Error Permitido\nEjemplo: 0.001',
                justify ='center')
    Error = Entry(window)
    err.place(x=105,y=220)
    Error.place(x=88, y=255)
    
    impresion = Label(window,textvariable=result,background = '#979191')
    
    #get data || call function#
    active = Button(window,
                    text="Calcular raiz",
                    command = lambda: result.set(secante(function.get(), float(intervaloA.get()), float(intervaloB.get()), float(Error.get()))))
    active.place(x=105,y=295)
    impresion.place(x=330 ,y= 70)
    #mainloop#
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
    window.config(cursor="circle")
    #image background
    canva = Canvas(window, width = 260, height = 320)
    canva.pack(fill = 'both', expand = True)
    canva.create_image(0,0, image = backg, anchor = 'nw')
    #botones para elegir
    system = Button(window, 
                text="Calculadora\nSistema de ecuaciones",
                command=windowsys)
    equation = Button(window,
                text="Calculadora\nEcuaciones no lineales",
                command=windowequ)
    system.place(x=65, y=145)
    equation.place(x=65, y=215)
    #mensaje
    asd = Label(window,
                text = "Bienvenido!",
                font = 'Candara -25 bold',
                background = '#979191',
                justify='center')
    asd.place(x=65, y=35)
    #ventana de secante o sistema
    window.mainloop()

window = mainWindow()