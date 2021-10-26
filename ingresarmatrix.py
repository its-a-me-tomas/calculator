coe = input("Ingresa la matrix->")
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
    
print(mat)

#-7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6 || -10;35;3;-6