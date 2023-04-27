import os

######### Etapa de depuracion

with open("initial_archive.txt", "r") as archivo_original:
    lineas = archivo_original.readlines()

with open("initial_archive_2.txt", "w") as archivo_modificado:
    for linea in lineas:
        linea_modificada = linea.replace('> Csirt2023:', '')
        linea_modificada = linea.replace('\n\n', '')
        linea_modificada = linea.replace('🖼 ', '')
        archivo_modificado.write(linea_modificada)

with open("initial_archive_2.txt", "r") as archivo_original:
    lineas = archivo_original.readlines()

with open("initial_archive_2.txt", "w") as archivo_modificado:
    for linea in lineas:
        linea_modificada = linea.replace('CSIRT-CEDIA Desfiguración:  ', '')
        archivo_modificado.write(linea_modificada)

with open("initial_archive_2.txt", "r") as archivo_original:
    lineas = archivo_original.readlines()

with open("initial_archive_2.txt", "w") as archivo_modificado:
    for linea in lineas:
        linea_modificada = linea.replace('CSIRT-CEDIA posible defacement:  ', '')
        archivo_modificado.write(linea_modificada)

with open("initial_archive_2.txt", "r") as archivo_original:
    lineas = archivo_original.readlines()

with open("initial_archive_2.txt", "w") as archivo_modificado:
    for linea in lineas:
        linea_modificada = linea.replace('> Csirt2023:', '')
        archivo_modificado.write(linea_modificada)

######### Etapa de eliminacion de duplicados

# Abrir archivo de entrada
with open('initial_archive_2.txt', 'r') as archivo_entrada:
    # Leer contenido del archivo
    contenido = archivo_entrada.read().splitlines()

# Eliminar duplicados
contenido_sin_duplicados = list(set(contenido))

with open('clean_links.txt', 'w') as archivo_salida:
    for linea in contenido_sin_duplicados:
        archivo_salida.write(linea + "\n")

# Eliminacion de archivos residuales

ruta_archivo = "initial_archive_2.txt"

if os.path.exists(ruta_archivo):
    os.remove(ruta_archivo)
    #print("Archivo eliminado exitosamente.")
else:
    print("El archivo no existe. ")
