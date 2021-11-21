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
definición del método
"""
def secante(func, a, b, err):
    def f(x):     #evaluar la función
        f = eval(func)
        return f
    ea, i, string = 1.0, 1, "" #variables auxiliares
    print("i \t r0 \t\t r1 \t\t ra \t\tError ") # impresión de la tabla
    string += " i \t r0 \t r1 \t ra \tError\n"
    print("------------------------------------------------------------------------")
    while ea > err: #inicio del método secante
        i += 1
        if i > 30:
            print("El método no converge")
            return "El método no converge"
            break
        ra = b - ((b-a)/(f(b)-f(a)))*f(b)
        ea = abs(ra-b)
        #rx = ra
        print("{}\t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f} ".format(i,a,b,ra,ea))
        string += " {} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f}\n".format(i,a,b,ra,ea)
        a=b
        b=ra
    print("\n Raiz en {:.6f} Iteraciones: {}".format(ra,i))
    string += "\n Raiz en {:.6f} Iteraciones: {}\n-------------------------------------------------------------".format(ra,i)
    print("------------------------------------------------------------------------")
    #fin método secante
    grafica(f,a,b,ra) #graficar la ecuación
    return string

#método grafica#
def grafica(fun,a,b,ra):
    x = np.linspace((a-5), (b+5), 500)
    y = fun(x)
    plt.plot(x,y)
    plt.plot([ra],[0], c='k', marker='.')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('Gráfica de la función')
    plt.grid(True)
    plt.show(block=False)