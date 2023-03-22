#------------Autor: Ignacio Miguel Sandalinas García------------
#-----------------------Fecha: 22.03.2023-----------------------

import csv

def read_data(nombreFicheroCSV):
    diccionarioRes = {}
    numeroClave = 1
    allDataInCSV = None

    with open(nombreFicheroCSV, 'r') as ficheroCSV:
        allDataInCSV = csv.reader(ficheroCSV)
        for row in allDataInCSV:
            estanTododsLosDatos = True
        
            for dataPiece in row:
                if dataPiece == "":
                    estanTododsLosDatos=False

            if estanTododsLosDatos == True:
                diccionarioRes["dato"+str(numeroClave)]={"type":row[0],"fixed acidity":row[1],"volatile acidity":row[2],"citric acid":row[3],"residual sugar":row[4],"chlorides":row[5],"free sulfur dioxide":row[6],"total sulfur dioxide":row[7],"density":row[8],"PH":row[9],"sulphates":row[10],"alcohol":row[11],"quality":row[12]}
                numeroClave+=1

    if numeroClave<11:
        raise ValueError("Ha ocurrido la excepción ValueError")

    return diccionarioRes

def split(wineDataDictionary):
    diccionarioWhiteRes = {}
    diccionarioRedRes = {}

    for wine in wineDataDictionary:
        if wine["type"]=="white":
            diccionarioWhiteRes[] = {}


    return diccionarioWhiteRes, diccionarioRedRes