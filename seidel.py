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
                graphic(len(a[0]),a,b,x0)
            return "El método no converge"
            break
    ######FIN MÉTODO GAUSS-SEIDEL#######
    if len(a[0]) > 3:
        text += "\nMás de tres dimensiones, no hay gráfica"
    else:
        graphic(len(a[0]),a,b,x0)
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
def graphic(dimension, matrix, independet, var):
    string = ''
    if dimension == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111,projection="3d")
        x, y = np.linspace(-8,8,100), np.linspace(-8,8,100)
        X, Y = np.meshgrid(x,y)
        for i in range(len(matrix)):
            z = (independet[i] - matrix[i][0]*X - matrix[i][1]*Y)/matrix[i][2]
            ax.plot_surface(X,Y,z, alpha=0.5, rstride=100, cstride=100)
        ax.set_xlabel('Eje x')
        ax.set_ylabel('Eje y')
        ax.set_zlabel('Eje z')
        plt.title('Gráfica de las ecuaciones')
        plt.show(block=False)
    elif dimension == 2:
        x, y = np.linspace(-10,10,500), np.linspace(-10,10,500)
        for i in range(len(matrix)):
            y = (independet[i]-matrix[i][0]*x)/matrix[i][1]
            if matrix[i][0] > 0:
                if i == range(len(matrix)):
                    string = 'x{}=('.format(i+1) + str(independet[i])+str(-matrix[i][0])+"x{})/".format(2)+str(matrix[i][1])
                else:
                    string = 'x{}=('.format(i+1) + str(independet[i])+str(-matrix[i][0])+"x{})/".format(1)+str(matrix[i][1])
            else:
                if i == range(len(matrix)):
                    string = 'x{}=('.format(i+1) + str(independet[i])+'+'+str(-matrix[i][0])+"x{})/".format(2)+str(matrix[i][1])
                else:
                    string = 'x{}=('.format(i+1) + str(independet[i])+'+'+str(-matrix[i][0])+"x{})/".format(1)+str(matrix[i][1])                
            plt.plot(x,y, label=string)
            print(string)
        plt.plot([0],[var[1]], c='k', marker='.')
        plt.plot([var[0]],[0], c='k', marker='.')
        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        plt.title('Gráfica de las ecuaciones')
        plt.legend()
        plt.grid(True)
        plt.show(block=False)