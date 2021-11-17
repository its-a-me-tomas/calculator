#Librerias necesarias
import numpy as np
from math import *
from sympy import * 
#lib for graphics
from matplotlib import pyplot as plt
""" Argumentos:
func = ecuación no lineal
a = intervalo menor
b = intervalo mayor
err = error permitido
definición del método """
def secante(func, a, b, err):
    def f(x):     #evaluar la función
        f = eval(func)
        return f
    ea, i = 1.0, 1 #variables auxiliares
    print("i \t r0 \t\t r1 \t\t ra \t\tError ") # impresión de la tabla
    print("------------------------------------------------------------------------")
    while ea > err: #inicio del método secante
        i += 1
        if i > 30:
            print("El método no converge")
            break
        ra = b - ((b-a)/(f(b)-f(a)))*f(b)
        ea = abs(ra-b)
        #rx = ra
        print("{}\t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f} ".format(i,a,b,ra,ea))
        a=b
        b=ra
    print("\n Raiz en {:.6f} Iteraciones: {}".format(ra,i))
    print("------------------------------------------------------------------------")
    #fin método secante
    grafica(func) #graficar la ecuación

#método grafica#
def grafica(fun):
    x = Symbol("x")
    f = fun
    plot(f,(x,-10,10))