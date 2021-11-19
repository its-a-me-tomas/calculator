#-7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6 || -10;35;3;-36 ejemplo de entrada
#lib for graphics
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
""" 
Argumentos:
a = matrix de coeficientes separados por espacios y punto y coma
b = vector de terminos independientes separados por punto y coma
e = error permitido
maxI = maximo de iteraciones 
"""

def siedel(a,b,e,maxI): #definición del método
    x0,x1=[],[]
    num = len(a)
    for i in range(num): #vector de aproximación auxiliar
        x0.append(0)
    k, err, imp, x1, text= 0, 1, "k\t", x0.copy(),"" #variables auxiliares
    for i in range(num): #impresión de la tabla
        imp +=  "x"+str(i+1)+"\t"
    print(imp+"error")
    print("------------------------------------------------\n")
    text += imp + "error\n"
    ######Método de Gauss-Seidel#######
    while err>e:
        k += 1
        impre = str(k)+"\t"
        for i in range(0,num):
            suma = b[i]
            for j in range(0,num):
                if i != j:
                    suma += -a[i][j]*x0[j]           
            x0[i] = suma/a[i][i]
            impre += "{:.6f}".format(x0[i])+"\t"
        err = abs(x0[i]-x1[i])
        x1=x0.copy()
        impre += "{:.5f}".format(err)+"\n"
        print(impre)
        text += impre
        if k > maxI:
            print("El método no converge")
            if len(a[0]) > 3:
                text += "\nMás de tres dimensiones, no hay gráfica"
            else:
                graphic(len(a[0]),a,b)
            return "El método no converge"
            break
    ######FIN MÉTODO GAUSS-SEIDEL#######
    if len(a[0]) > 3:
        text += "\nMás de tres dimensiones, no hay gráfica"
    else:
        graphic(len(a[0]),a,b)
    return text
    
#conversor de string a matrix
def converA(coe):
    mat = []
    sr,k = "", 0
    coe+=" "
    for i in range(coe.count(";")+1):
        arr = []
        for x in coe:
            k+=1
            if x == "-" or x != " " and x != ";":
                sr += x
                #print(sr)
            elif x == " " or x ==";":    
                arr.append(float(sr))
                #print(arr)
                sr = ""
            if x == ";":
                coe = coe[k:len(coe)]
                k=0
                break
        mat.append(arr)
    return mat

#conversor de string a vector
def converB(array):
    sr= ""
    array += " "
    arreglo = []
    for x in array:
        if x == "-" or x != " " and x != ";":
            sr += x
            #print(sr)
        elif x ==";" or x == " ":    
            arreglo.append(float(sr))
            #print(arreglo)
            sr = ""
    #print(arreglo)
    return arreglo

#grafica#
#grafica dinamica para n ecuaciones#
def graphic(dimension, matrix, independet):
    if dimension == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111,projection="3d")
        x, y = np.linspace(-8,8,100), np.linspace(-8,8,100)
        X, Y = np.meshgrid(x,y)
        for i in range(len(matrix)):
            z = (independet[i] - matrix[i][0]*X - matrix[i][1]*Y)/matrix[i][2]
            ax.plot_surface(X,Y,z, facecolors='b', alpha=0.5, rstride=100, cstride=100)
        plt.show()
    elif dimension == 2:
        x, y = np.linspace(-10,10,500), np.linspace(-10,10,500)
        for i in range(len(matrix)):
            y = (independet[i]-matrix[i][0]*x)/matrix[i][1]
            plt.plot(x,y)
        plt.show()    