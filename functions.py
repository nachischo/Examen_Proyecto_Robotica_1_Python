import csv

def read_data(nombreFicheroCSV):
    diccionarioRes = {}
    numeroClave = 1
    allDataInCSV = None

    with open(nombreFicheroCSV, 'r') as ficheroCSV:
        allDataInCSV = csv.reader(ficheroCSV)
        for row in allDataInCSV:
            diccionarioRes["dato"+str(numeroClave)]={"type":row[0],"fixed acidity":row[1],"volatile acidity":row[2],"citric acid":row[3],"type":row[4]}
            numeroClave+=1

    
    

    

    return diccionarioRes