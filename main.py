# invocar a los archivos para los métodos
from seidel import *
from secante import *
#librerias para la interfaz grafica (aun trabajando)
import tkinter as tk
#from tkinter import ttk

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
root = tk.Tk()
root.withdraw()
current_window  = None
####   windows   ####
def windowsys(): #sistema de ecuaciones#
    global current_window
    if current_window is not None:
        current_window.destroy()
    current_window = tk.Toplevel(root)
    current_window.wm_protocol("WM_DELETE_WINDOW", mainWindow)
    window = current_window
    #properties
    window.iconbitmap('Calculator.ico')
    window.title('Calculadora de Sistemas de ecuaciones no lineales')
    window.resizable(0,0)
    window.geometry("720x420")
    #extra settings
    window.config(cursor="pirate")
    #mensaje
    asd = tk.Label(window, text="¡Hola,Bienvenido a la Calculadora de sistema de ecuaciones y sistemas no lineales!")
    asd.place(x=130, y=50, width=450, height=20)
    #entrada de datos
    a = tk.Entry(window, width=50)
    a.place(x=130, y=200, width=50)
    b = tk.Entry(window, width=50)
    b.place(x=130, y=230, width=50)
    ea = tk.Entry(window, width=50)
    ea.place(x=130, y=260, width=50)
    maxI = tk.Entry(window, width=50)
    maxI.place(x=130, y=290, width=50)
    #llamada a function#
    
    #ventana de secante o sistema
    window.mainloop()

def windowequ():  #ecuaciones no lineales#
    global current_window
    if current_window is not None:
        current_window.destroy()
    current_window = tk.Toplevel(root)
    current_window.wm_protocol("WM_DELETE_WINDOW", mainWindow)
    window = current_window
    window.iconbitmap('Calculator.ico')
    window.title('Calculadora de sistemas de ecuaciones')
    window.resizable(0,0)
    window.geometry("720x420")
    #extra settings
    window.config(cursor="pirate")
    #mensaje
    asd = tk.Label(window, text="¡Hola,Bienvenido a la Calculadora de sistema de ecuaciones!")
    asd.place(x=130, y=50, width=450, height=20)
    #entrada de datos
    fun = tk.Entry(window, width=50)
    fun.place(x=130, y=200, width=50)
    a = tk.Entry(window, width=50)
    a.place(x=130, y=230, width=50)
    b = tk.Entry(window, width=50)
    b.place(x=130, y=260, width=50)
    ea = tk.Entry(window, width=50)
    ea.place(x=130, y=290, width=50)
    #llamada a function#
    window.mainloop()

def mainWindow():
    global current_window
    if current_window is not None:
        current_window.destroy()
    current_window = tk.Toplevel(root)
    current_window.wm_protocol("WM_DELETE_WINDOW", root.destroy)
    window = current_window #crea ventana    
    window.iconbitmap('Calculator.ico')
    window.title('Calculadora de Sistemas de sistemas de ecuaciones')
    window.resizable(0,0)
    window.geometry("720x420")
    #extra settings
    window.config(cursor="pirate")

    #botones para elegir
    pto = tk.Button(window, text="Sistema de ecuaciones", command=windowsys)
    pto2 = tk.Button(window, text="Ecuacion no lineal", command=windowequ)
    pto.place(x=120, y=205)
    pto2.place(x=400, y=205)
    #mensaje
    asd = tk.Label(window, text="¡Hola,Bienvenido a la Calculadora de sistema de ecuaciones y sistemas no lineales!")
    asd.place(x=130, y=50, width=450, height=20)
    #ventana de secante o sistema
    window.mainloop()

window = mainWindow()

# #properties
# root.iconbitmap('Calculator.ico')
# root.title('Calculadora de Sistemas de ecuaciones no lineales y sistemas de ecuaciones')
# root.resizable(0,0)
# root.geometry("720x420")
# #extra settings
# root.config(cursor="pirate")

# #botones para elegir
# pto = tk.Button(root, text="Sistema de ecuaciones", command=windowsys)
# pto2 = tk.Button(root, text="Ecuacion no lineal", command=windowequ)
# pto.place(x=120, y=205)
# pto2.place(x=400, y=205)
# #mensaje
# asd = tk.Label(root, text="¡Hola,Bienvenido a la Calculadora de sistema de ecuaciones y sistemas no lineales!")
# asd.place(x=130, y=50, width=450, height=20)
# #ventana de secante o sistema

# root.mainloop() #principal