# invocar a los archivos para los métodos
from seidel import *
from secante import *
#librerias para la interfaz grafica (aun trabajando)
#from tkinter import *
#from tkinter import ttk

#Opciones para la calculadora
inp = int(input("solución de sistema de ecuaciones(2) o raiz de ecuación no lineal(1)->"))
#raiz de ecuaciones no lineales secante#
if inp == 1:
    fun = input("Ingresa la función-->")
    a = float(input("1er Aproximación Inicial ->"))
    b = float((input("2da Aproximación Inicial ->")))
    ea = float((input("Error permitido ->")))
    secante(fun, a, b, ea)
#seidel Sistemas de ecuaciones
elif inp == 2 :
    a = converA(input("Ingrese la matriz de coeficientes->"))
    b = converB(input("Ingresa el vector de términos independientes->"))
    e = float(input("Error permitido->"))
    maxI = int(input("Máxima de iteraciones->"))
    seidel(a,b,e,maxI)


"""
Interfaz en proceso
#-7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6 || -10;35;3;-6
 
root = Tk()
#properties
root.iconbitmap('Calculator.ico')
root.title('Calculadora de Sistemas de ecuaciones no lineales y sistemas de ecuaciones')
root.resizable(0,0)
root.geometry("720x420")
#extra settings
root.config()
root.mainloop()  
"""