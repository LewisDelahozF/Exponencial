import sys

ruta = 'A20.txt'

#print (archivo.read())
"""
if len(sys.argv) < 3:
    print("Faltan argumentos")
    print("Deben ir de la siguiente forma: potencia lenguaje")
else:
    texto = sys.argv[2]
    num = sys.argv[1]"""

texto = "b"

texto = texto.replace("{","")
texto = texto.replace("}","")
texto = texto.replace(","," ")

lenguaje = texto.split()
lenguajeAnterior = lenguaje
num = 20

def guardararchivo(lenguaje,potencia):
    archivo = open(ruta, 'a')
    archivo.write("potencia ")
    archivo.write(str(potencia))
    archivo.write(" = {")
    posicion = 0
    limite = len(lenguaje)-1
    for x in lenguaje:
        if (posicion < limite):
            x = x + ","
        archivo.write(x)
        posicion+=1
    archivo.write("}\n")
    archivo.close()



def potencia(lenguajeelev, exponente):
    global num
    if(exponente < num):
        global lenguaje
        global lenguajeAnterior
        aux = []
        for x in lenguaje:
            for y in lenguajeelev:
                aux.append(x+y)
        lenguajeAnterior = lenguajeelev + aux
        guardararchivo(lenguajeAnterior, exponente+1)
        print("potencia ", exponente+1, " = ", lenguajeAnterior)
        input("Pulsa Enter para continuar...")
        potencia(lenguajeAnterior, exponente+1)


potencia(lenguaje,1)
