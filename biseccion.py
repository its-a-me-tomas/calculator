#Librerias necesarias
import numpy as np
from math import *
from sympy import * 
#Argumentos:
#func = ecuación no lineal
#a = intervalo menor
#b = intervalo mayor
#err = error permitido
#definición del método
def biseccion(func, a, b, err): 
    def f(x):     #evaluar la función
        f = eval(func)          
        return f                
    ea, ra, i, rx = 1.0, (a+b)/2, 1, 0.0 #variables auxiliares
    print("i \t a \t\t b \t\t ra \t\t f(ra) \t\t f(a) \t\t f(b) \t\t Error") # impresión de la tabla
    print("------------------------------------------------------------------------")
    print("{}\t {:.4f} \t {:.5f} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f}".format(i,a,b,ra,f(ra),f(a),f(b),ea))
    if f(a)*f(b) < 0 : #evaluación del los intervalos
        while ea > err: #inicio del método bisección
            i += 1
            if f(a)*f(ra) < 0:
                b = ra
            else:
                a =ra
            ra = (a+b)/2
            ea = abs(rx-ra)
            rx = ra
            print("{}\t {:.4f} \t {:.5f} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f}".format(i,a,b,ra,f(ra),f(a),f(b),ea))
        print("\n Raiz en {:.6f} Iteraciones: {}".format(ra,i))
        print("------------------------------------------------------------------------")
        #fin método bisección
        grafica(func) #graficar la ecuación
    else:
        print('No hay raíz en el intervalo dado')

#método grafica#
def grafica(fun):
    x = Symbol("x")
    f = fun
    plot(f,(x,-10,10))