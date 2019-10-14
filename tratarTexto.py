import csv, operator
import codecs
import json
file = codecs.open('CandidatosElectos-2019-04.csv', 'r','cp1252')
entrada = csv.reader(file, delimiter=';')
candidaturas = {}
candidaturas['cuentas'] =[]
for row in entrada:
    cuenta ={}
    candidaturaNew = ""
    provinciaNew = ""
    candidatura, provincia, candidatos, nombre, twitter, web, facebook = row
    if candidatura !='':
        candidaturaNew = candidatura
    if provincia !='':
        provinciaNew = provincia
    cuenta["candidatura"] = candidaturaNew
    cuenta["provincia"] = provinciaNew
    cuenta["nombre"] = nombre
    cuenta["twitter"] = twitter
    cuenta["web"] = web
    cuenta["facebook"] = facebook
    candidaturas['cuentas'].append(cuenta)
file.close()

with open("cuentas.json","w") as results_file:
    json.dump(candidaturas, results_file, indent=4, sort_keys=True, ensure_ascii=False)

with open("cuentas.json", "r") as json_file:
    data = json.load(json_file)
    for p in data['cuentas']:
        print ("Nombre: "+ p['nombre'])
        print ("Twitter:" + p['twitter'])
    json_file.close()