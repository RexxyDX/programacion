num=int(input("Cuantos numeros desea agregar?\n"))
p=0
i=0
total=0
for x in range(num):
    o=int(input("Que numero desea agregar?\n"))
    print(o)
    total=total+o
    print("La suma total de todos sus digitos va en:", total)
    if o%2==0:
        p=p+o
    else:
        i=i+o

print("La suma de los numeros pares es:", p)

print("La suma de los numeros impares es:", i)