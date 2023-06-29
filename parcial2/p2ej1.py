#Construir un algoritmo que permita generar enteros de 3 en 3 comenzado por el 2 hasta el
#valor máximo que será menor que 30. Calcular la suma de los enteros generados que sean
#divisibles por 5, y la suma de los enteros generados que sean impares

#generador de numeros 

max = 30

def enteros_tres(max):
    numero = 2
    while numero < max:
        print(numero)
        numero += 3
enteros_tres(max)

#indicador de los divisibles e impares

dividido = 0
impares = 0
for i in range (2, max, 3) :
     if i % 5 == 0 :
        dividido  += i
     if i % 2 != 0 :
        impares += i

print("total de numeros que son divisibles por 5")
print(dividido)

print("numero de impares")
print(impares)