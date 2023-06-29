#3. Se cuenta con dos sets, los cuales contienen precios de productos: (40 Puntos)
#Set 1 = {100, 250, 300, 1000}
#Set 2 = {150, 250, 500, 1000}

set1 = {100, 250, 300, 1000}
set2 = {150, 250, 500, 100}

#A) Verificar si el valor 100 está en ambos sets

if 100 in set1 and 100 in set2:
    print ("el numero 100 esta en los dos sets")
else:
     print("el numero 100 no esta en ambos sets")

#B) Comprobar si al menos el valor 500 o 700 está en alguno de los sets
  
if 500 in set1 or 500 in set2 or 700 in set1 or 700 in set2:
     print("el numero 500 o 700 esta en uno de los sets")
else: 
     print("ninguno de los numeros esta en los sets")

#C) Elevar a 3 todos los valores dentro de los sets

set1 = {x ** 3 for x in set1}
set2 = {x ** 3 for x in set2}

print ("al elevar a 3 el set 1, el resultado es")
print (set1)

print ("al elevar a 3 el set 2, el resultado es")
print (set2)

#D) Unir ambos sets en uno solo

newset = set1.union(set2)
print ("el resultado del set unido es")
print (newset)



