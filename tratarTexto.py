import csv, operator
import codecs
import json
file = codecs.open('CandidatosElectos-2019-04.csv', 'r','cp1252')
entrada = csv.reader(file, delimiter=';')
candidaturas = []
for row in entrada:
    cuenta = {}
    candidatura, provincia, candidatos, nombre, twitter, web, facebook = row

    if candidatura !='':
        candidaturaNew = candidatura
    if provincia !='':
        provinciaNew = provincia
    cuenta["candidatura"] = candidaturaNew
    cuenta["povincia"] = provinciaNew
    cuenta["nombre"]= nombre
    cuenta["twitter"]= twitter
    cuenta["web"]= web
    cuenta["facebook"]=facebook
    print (cuenta["twitter"])
    candidaturas.append(cuenta)
file.close()
with open("results.json","w") as results_file:
    json.dump(candidaturas, results_file, indent=4, sort_keys=True, ensure_ascii=False)
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