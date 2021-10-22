coe = input("Ingresa la matrix separada por espacios y ; ->")
a = []
for x in coe:
    aa = [] 
    if x != " " or x !=",":
        aa.append(str(x))
    elif x == ";":
        a.append(aa)
print(a)
b = [[-10],[35],[3],[-6]]
e = 0.0001
maxI = 30
x0=[]

#[[-7,-4,-1,-1],[-1,8,-5,0],[-1,-2,-4,0],[0,2,0,-6]] [-10,35,3,-6]
num = len(matrix)
print(num)
for i in range(num):
    x0.append(0)
k, err, x1, imp = 0,1,x0,""    
for i in range(num):
    imp +=  "x"+str(i)+"\t"
print(imp+"error\n")
print("------------------------------------------------\n")
######Método de Gauss-Seidel#######
while err>e:
    k = k+1
    impre = ""
    for i in range(num):
        impre
        suma = 0
        for j in range(i-1):
            suma = suma + matrix(i,j)*x0(j)
        suma2=0
        j=i+1
        for j in range(num):
            suma2 = suma2 + matrix(i,j)*x0(j)
        impre += str(x0(i))+"\t"
    err = abs(x0(i)-x1(i))
    x1=x0
    impre += str(err)+"\n"
    print(impre)
    if k > maxI:
        print("El método no converge")
        break

class toArray():
    def converA(matrix):
        mat = []
        sr, k = "",0
        for i in range(coe.count(";")):
            arr = []
            x = k
            for x in coe:
                k += 1
                if x == "-" or x != " " and x != ";":
                    sr += x
                    #print(sr)
                elif x == " " or x ==";":    
                    k += 1
                    arr.append(float(sr))
                    print(arr)
                    sr = ""
                if x == ";":
                    break
            mat.append(arr)
        return mat
    def converB(array):
        sr= ""
        arreglo = []
        for x in array:
            if x == "-" or x != " " and x != ";":
                sr += x
                print(sr)
            elif x ==";":    
                arreglo.append(float(sr))
                print(arreglo)
                sr = ""
        return arreglo
