#inverso: stn -> stn
#Escribe una palabra y se
#entregara la misma pero invertida
#escribir un string y lo devuelva invertido
#ej: inverso(roma) entrega amor
def inverso(lista, n=0):
    if n==len(lista):
        return lista
    else:
        lista[n] = lista[n][::-1]
        n += 1
        return inverso(lista, n)

lst= ["rata"]
print(inverso(lst))

#se uso un nombre generico para la funcion y
#al ejecutarse ahora tiene una palabra la cual es
#legible de forma inversa, a diferencia del papel el
#imput se modifico agregando asi informacion no presente
#al programar en papel.
