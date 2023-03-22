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
    whiteWineCount = 1
    diccionarioRedRes = {}
    redWineCount=1

    for wine in wineDataDictionary:
        
        if wineDataDictionary[wine]["type"]=="white":
             diccionarioWhiteRes["dato"+str(whiteWineCount)] = {"fixed acidity":wineDataDictionary[wine]["fixed acidity"],"volatile acidity":wineDataDictionary[wine]["volatile acidity"],"citric acid":wineDataDictionary[wine]["citric acid"],"residual sugar":wineDataDictionary[wine]["residual sugar"],"chlorides":wineDataDictionary[wine]["chlorides"],"free sulfur dioxide":wineDataDictionary[wine]["free sulfur dioxide"],"total sulfur dioxide":wineDataDictionary[wine]["total sulfur dioxide"],"density":wineDataDictionary[wine]["density"],"PH":wineDataDictionary[wine]["PH"],"sulphates":wineDataDictionary[wine]["sulphates"],"alcohol":wineDataDictionary[wine]["alcohol"],"quality":wineDataDictionary[wine]["quality"]}
             whiteWineCount+=1

        elif wineDataDictionary[wine]["type"]=="red":
            diccionarioRedRes["dato"+str(redWineCount)] = {"fixed acidity":wineDataDictionary[wine]["fixed acidity"],"volatile acidity":wineDataDictionary[wine]["volatile acidity"],"citric acid":wineDataDictionary[wine]["citric acid"],"residual sugar":wineDataDictionary[wine]["residual sugar"],"chlorides":wineDataDictionary[wine]["chlorides"],"free sulfur dioxide":wineDataDictionary[wine]["free sulfur dioxide"],"total sulfur dioxide":wineDataDictionary[wine]["total sulfur dioxide"],"density":wineDataDictionary[wine]["density"],"PH":wineDataDictionary[wine]["PH"],"sulphates":wineDataDictionary[wine]["sulphates"],"alcohol":wineDataDictionary[wine]["alcohol"],"quality":wineDataDictionary[wine]["quality"]}
            redWineCount+=1

    return diccionarioWhiteRes, diccionarioRedRes

def reduce(wineDataDictionary, dataTypeWanted):
    wantedAttributeListRes = []

    for wine in wineDataDictionary:
        if dataTypeWanted in wineDataDictionary[wine]:
            raise ValueError("Ha ocurrido la excepción ValueError")
        
        wantedAttributeListRes.append(wineDataDictionary[wine][dataTypeWanted])

    return wantedAttributeListRes

def silhouette():

    return
