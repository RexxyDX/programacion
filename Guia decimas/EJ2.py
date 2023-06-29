def ingresar_nombres():
    
    x=[]
    
    while True:
        nombre=input("Escriba un nombre o detener para dejar de ingresar nombres\n")
        if nombre == "DETENER":
            break
        else:
            x.append(nombre)
    return x

    
def contar_letras(list):
    
    list2=[]
    
    for i in range(0,len(list)):
        list2.append(len(list[i]))
    return(list2)

def mostrar_resultados(nombre,list3):

    print("Los nombres ingresados y las letras contadas son")
    for i in range(0,len(nombre)):
        print("Nombres",nombre[i],"    ","Letras",list3[i])
        
    print("total de letras es")
    print(sum(list3))
   
list_new=ingresar_nombres()
mostrar_resultados(list_new,contar_letras(list_new))