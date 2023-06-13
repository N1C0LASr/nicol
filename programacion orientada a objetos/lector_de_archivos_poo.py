nombre_archivo = 'programacion orientada a objetos/texto_de_prueba.txt'
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read() 
    print (contenido)