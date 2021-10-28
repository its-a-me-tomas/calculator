#-7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6 || -10;35;3;-36 ejemplo de entrada
#Argumentos:
# a = matrix de coeficientes separados por espacios y punto y coma
# b = vector de terminos independientes separados por punto y coma
# e = error permitido
# maxI = maximo de iteraciones

def siedel(a,b,e,maxI): #definición del método
    x0,x1=[],[]
    num = len(a)
    for i in range(num): #vector de aproximación auxiliar
        x0.append(0)
    k, err, imp, x1 = 0, 1, "k\t", x0.copy() #variables auxiliares
    for i in range(num): #impresión de la tabla
        imp +=  "x"+str(i+1)+"\t\t"
    print(imp+"error")
    print("------------------------------------------------\n")
    ######Método de Gauss-Seidel#######
    while err>e:
        k = k+1
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
        if k > maxI:
            print("El método no converge")
            break
    ######FIN MÉTODO GAUSS-SEIDEL#######
    
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
