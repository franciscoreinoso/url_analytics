## Lectura y segmentacion de informacion en reportes

import os

input_file = "report1682260876705.txt"

vector = []

# Primera etapa: Obtencion de dominios/institutos receptores

#print("\nPrimera Etapa \n")

with open(input_file, "r") as f, open("suitable_report.txt", "w") as out:
    out.write('"Device Time","File Name","Malware Name","Mail Receiver","Mail Sender","Source IP"\n')
    lines = f.readlines()[1:]
    for line in lines:
        arg1 = line.split(',')[0].strip('"')
        arg2 = line.split('"')[5].strip('"') ##
        arg3 = line.split('"')[3].strip('"').replace(',', '.')
        arg4 = line.split('"')[7].strip('"')
        arg5 = line.split('"')[9].strip('"')
        arg6 = line.split(',')[-1].strip('"').replace('"', '').replace('\n', '')
        out.write('"' + arg1 + '","' + arg3 + '","' + arg2 + '","' + arg4 + '","' + arg5 + '","' + arg6 + '"\n')

input_file = "suitable_report.txt"
output_file = "analisis.txt"

with open(input_file, "r") as f, open(output_file, "w") as out:
    lines = f.readlines()[1:]
    for line in lines:
        primer_argumento = line.split(',')[3].strip('"')
        source = line.split(',')[4].strip('"')
        IP = line.split(',')[5].strip('"').replace('"', '').replace('\n', '')
        #print("Line " + primer_argumento)
        dominio = primer_argumento.split("@")[1]
        #print(dominio + "," + source + "," + IP)
        out.write(dominio + "," + source + "," + IP + "\n")

## Ordenamiento

with open('analisis.txt', 'r') as f:
    contenido = f.readlines()

contenido_ordenado = sorted(contenido)

with open('analisis2.txt', 'w') as f:
    f.writelines(contenido_ordenado)

# Segunda etapa: Separacion de dominios

print("\nResultados ejecucion \n")

input_file = "analisis2.txt"

with open(input_file, "r") as f:
    for line in f:
        primer_argumento = line.split(',')[0]
        vector.append(primer_argumento)
        #print(primer_argumento)

vector2 = list(set(vector))
vector2 = sorted(vector2)           ## Vector de total de dominios afectados
print("Total de dominios listados/afectados: " + str(vector2))

## Tercera etapa: Ordenamiento de informacion

with open("Reporte_filtrado.txt", "w") as f:
    f.write("\n \t \t \tListado de Instituciones con registros de posible phishing \n")
    for i in range(len(vector2)):
        print("\nInstitucion destino: \t \t" + vector2[i] + "\n")
        f.write("\n" + "Target/Affected Institution: \t \t " + vector2[i] + "\n \n")
        input_file = "analisis2.txt"

        with open(input_file, "r") as f2:
            for line in f2:
                source = line.split(',')[1].strip('"')
                IP = line.split(',')[2].strip('"').replace('"', '').replace('\n', '')
                argumento = line.split(',')[0]
                if argumento == vector2[i]:
                    print("Mail Sender: " + source + ", Source IP: " + IP)
                    f.write("Mail Sender: " + source + ", Source IP: " + IP + "\n")


# Eliminacion de archivos residuales

archivos = ["analisis.txt", "analisis2.txt", "suitable_report.txt"]

for ruta_archivo in archivos:
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)
    else:
        print(f"El archivo {ruta_archivo} no existe.")
