from seidel import *
from biseccion import *

from tkinter import *
from tkinter import ttk

inp = int(input("solución de sistema de ecuaciones(2) o raiz de ecuación no lineal(1)->"))
if inp == 1:
    fun = input("Ingresa la función-->")
    a = float(input("Intervalo menor ->"))
    b = float((input("Intervalo mayor ->")))
    ea = float((input("Error permitido ->")))
    biseccion(fun, a, b, ea)
#ecuaciones no lineales bisección#
elif inp == 2 :
#seidel ecuaciones lineales#
    a = converA(input("Ingrese la matriz de coeficientes->"))
    b = converB(input("Ingresa el vector de términos independientes->"))
    e = float(input("Error permitido->"))
    maxI = int(input("Máxima de iteraciones->"))
    metodo(a,b,e,maxI)


"""
#-7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6 || -10;35;3;-6
[[-7,-4,-1,-1],[-1,8,-5,0],[-1,-2,-4,0],[0,2,0,-6]] 
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