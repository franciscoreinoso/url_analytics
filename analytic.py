import requests

# Inicializacion de variables y vectores
active = []
inactive = []

# Definir el archivo de entrada y salida
input_file = "clean_links.txt"
output_file = "test_result.txt"

# Leer el archivo de entrada y obtener los enlaces
with open(input_file, "r") as f:
    enlaces = f.readlines()

# Verificar cada enlace y guardar los válidos en el archivo de salida
with open(output_file, "w") as f:
    for enlace in enlaces:
        enlace = enlace.strip()  # Eliminar saltos de línea
        try:
            response = requests.get(enlace)
            if response.status_code == 200 or response.status_code == 406:
                print(enlace + " : SI carga correctamente")
                active.append(enlace)
                f.write(enlace + " : SI carga correctamente (código de estado " + str(response.status_code) + ")" + "\n")
                f.write("_____________________________________\n")
            else:
                inactive.append(enlace)
                print(enlace + " : NO carga correctamente (código de estado " + str(response.status_code) + ")")
                f.write(enlace + " : NO carga correctamente (código de estado " + str(response.status_code) + ")" +  "\n")
                f.write("_____________________________________\n")
        except requests.exceptions.RequestException as e:
            inactive.append(enlace)
            print(enlace + " : NO carga correctamente (" + str(e) + ")")
            f.write(enlace + " : NO carga correctamente (" + str(e) + ")")
            f.write("\n_____________________________________\n")


with open("defacementlist.txt", "w") as f:
    f.write("\n \tLista de dominios con afectacion de defacement activas e inactivas\n \n")
    ## Segmentacion de enlaces activos en archivo resultante
    f.write("Dominios Activos:\n \n")
    for i in range(len(active)):
        f.write(active[i] + "\n")
    ## Segmentacion de enlaces activos en archivo resultante
    f.write("\nDominios Inactivos/Dados de Baja/Inaccesibles:\n \n")
    for i in range(len(inactive)):
        f.write(inactive[i] + "\n")




