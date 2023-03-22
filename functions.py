import csv

def read_data(nombreFicheroCSV):

    allDataInCSV = csv.reader(nombreFicheroCSV)
    diccionarioRes = {}
    numeroClave = 1

    for row in allDataInCSV:
        diccionarioRes["dato"+str(numeroClave)]

    return diccionarioRes