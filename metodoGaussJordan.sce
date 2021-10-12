

a = input("ingresar matriz aumentada -->")
[i,j] = size(a)
disp(a,"Matriz ingresada:")
//algoritmo de Gauss-jordan
for k = 1 : i
    //pivote
    a(k,:) = a(k,:)/a(k,k)
    //operaciones de renglones
    for it = 1 : i
        if it <> k
            a(it,:) = a(it,:)-a(it,k)*a(k,:)
        end
    end
    disp(a)
end
//solucion
for l = 1 : i
    sol(l) = a(l,i+1) 
end
//Mostrar
for l = 1 : i
    sol1 = sol(l)
    printf("\nX%d=",l)
    disp(sol1)
end
disp(a);
