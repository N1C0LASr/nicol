#esCapicua palabra==palabra
#al ingresar una palabra
#y se verifique que es igual estando
#escrita de forma normal e inversa

def esCapicua(palabra):
    a = 0
    b = len(palabra) - 1
    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False

    return True

palabra = input("ingrese una palabra: ")

if esCapicua(palabra):
    print("True")
else:
    print("False") 
    
#Sere sincero las mejoras o similitudes en cuanto
#al codigo es por la informacion pasada en clases previas
#pero en escencia las mejoras serian en cuanto a
#la descripcion de que hace el programa y que funcione
