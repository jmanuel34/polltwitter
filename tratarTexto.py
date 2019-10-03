import csv, operator
file = open('Representantes.csv')
entrada = csv.reader(file, delimiter = ';')
for row in entrada:
    candidatura, provincia, candidatos, nombreyApellidos=row
    print ("Candidatura " + candidatura, "Provincia "+provincia, "Nombre "+ nombreyApellidos)

file.close()
"""
reg = next(entrada)  # Leer registro (lista)
print(reg)  # Mostrar registro

candidatura, provincia, candidatos, nombreyApellidos=next(entrada)
#nombre, provincia, consumo = next(entrada)  # Leer campos
print(candidatura, provincia, candidatos, nombreyApellidos)  # Mostrar campos

#del nombre, provincia, consumo, entrada  # Borrar objetos
csvarchivo.close()  # Cerrar archivo
#del csvarchivo  # Borrar objeto
"""