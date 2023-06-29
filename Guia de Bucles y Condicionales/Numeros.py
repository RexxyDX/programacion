a= [10,9,12,15,18]
b= [21,8,15,3,12]

con= a+b
print("Lista Concateneada: ",con)

con.insert(1,30)
print("Lista con el numero 30: ", con)

con.sort()
print("Lista Ordenada: ", con)

con.append([4,5,6])
print("Lista con los digitos 4,5 y 6: ", con)

suma= sum(con[:con.index([4, 5, 6])])
print("Suma total de la lista:", suma)

lon= len(con)
med= suma/longitud

if lon % 2 == 0:
    meda = (con[lon // 2 - 1] + con[lon // 2]) / 2
else:
    meda = con[lon // 2]

print("Media:", med)
print("Mediana:", meda)



