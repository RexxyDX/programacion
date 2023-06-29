def Bisiesto(x):
    if x%4==0:
        print(x, "Es un año Bisiesto")
    else:
        print(x, "No es un año Bisiesto")

año=int(input("Que año quieres verificar si es o no bisiesto\n"))
Bisiesto(año)