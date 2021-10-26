import numpy as np
from math import *

def biseccion(func, a, b, err):
    def f(x):
        f = eval(func)
        return f
    ea, ra, i, rx = 1.0, (a+b)/2, 1, 0.0
    print("i \t a \t\t b \t\t ra \t\t f(ra) \t\t f(a) \t\t f(b) \t\t Ea")
    print("------------------------------------------------------------------------")
    print("{}\t {:.4f} \t {:.5f} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f}".format(i,a,b,ra,f(a),f(b),f(ra),ea))
    if f(a)*f(b) < 0 :
        while ea > err:
            i += 1
            if f(a)*f(ra) < 0:
                b = ra
            else:
                a =ra
            ra = (a+b)/2
            ea = abs(rx-ra)
            rx = ra
            print("{}\t {:.4f} \t {:.5f} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f}".format(i,a,b,ra,f(a),f(b),f(ra),ea))
        print("\n Raiz en {:.6f} Iteraciones: {}".format(ra,i))
        print("------------------------------------------------------------------------")
    else:
        print('No hay raíz en el intervalo dado')
    #Investigar grafica#
