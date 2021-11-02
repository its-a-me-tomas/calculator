# invocar a los archivos para los métodos
from seidel import *
from secante import *
#librerias para la interfaz grafica (aun trabajando)
from tkinter import *
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

####   windows   ####
def windowsys():
     sys = Toplevel(root)
     labelExample = Label(sys, text="Sistemas de ecuaciones")
     buttonExample = Button(sys, text="Resolve")

     labelExample.pack()
     buttonExample.pack()
     sys.resizable(False, False)
     sys.geometry("600x420")
     sys.config(cursor="pirate")
     sys.iconbitmap('Calculator.ico')

def windowequ():
     equ = Toplevel(root)
     labelExample = Label(equ, text="Ecuaciones no lineales")
     buttonExample = Button(equ, text="Resolve")

     labelExample.pack()
     buttonExample.pack()

     equ.resizable(False, False)
     equ.geometry("600x420")
     equ.config(cursor="pirate")
     equ.iconbitmap('Calculator.ico')


root = Tk() #inicializar
#properties
root.iconbitmap('Calculator.ico')
root.title('Calculadora de Sistemas de ecuaciones no lineales y sistemas de ecuaciones')
root.resizable(0,0)
root.geometry("720x420")
#extra settings
root.config(cursor="pirate")

#botones para elegir
pto = Button(root, text="Sistema de ecuaciones", command=windowsys)
pto2 = Button(root, text="Ecuacion no lineal", command=windowequ)
pto.place(x=120, y=205)
pto2.place(x=400, y=205)
#mensaje
asd = Label(root, text="¡Hola,Bienvenido a la Calculadora de sistema de ecuaciones y sistemas no lineales!")
asd.place(x=130, y=50, width=450, height=20)
#ventana de secante o sistema

root.mainloop() #principal