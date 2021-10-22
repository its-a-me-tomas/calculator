coe = input("Ingresa la matrix ->")
sr= ""
aa = []
for x in coe:
    if x == "-" or x != " " and x != ";":
        sr += x
        print(sr)
    elif x ==";":    
        aa.append(float(sr))
        print(aa)
        sr = ""
    
   
print(aa)
#-7 -4 -1 -1;-1 8 -5 0;-1 -2 -4 0;0 2 0 -6 || -10;35;3;-6