#reto 7

def funcion(frase):
    palabras = frase.split()
    longitud = map(len,palabras)
    return dict(zip(palabras,longitud))
print(funcion(input("escriba una palabra")))