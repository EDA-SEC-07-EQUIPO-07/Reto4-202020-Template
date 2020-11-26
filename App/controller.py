import config as cf
from App import model
import csv
import os
# ___________________________________________________
#  Inicializacion del catalogo
def InitCatalog():
    Analyzer = model.analyzer()
    return Analyzer
# ___________________________________________________


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
def loadTrips(analyzer, filename):
    archivos = []
    print(filename)
    cargar = loadFile(analyzer, filename)
    Arcos = model.TotalDeArcos(analyzer)
    Vertices = model.TotalDeVertices(analyzer)
    Clusters = model.TotaldeClusteres(analyzer)
    archivos.append({"Total de Vertices":Vertices})
    archivos.append({"Total de Arcos":Arcos})
    archivos.append({"Total de Clusters":Clusters})
    return archivos
def loadFile(analyzer, file):
    """
    """
    file = cf.data_dir + file
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for route in input_file:
        model.AñadirRuta(analyzer, route)
    return analyzer

# ___________________________________________________

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def totalClusters(analyzer):
    retorno = model.TotaldeClusteres(analyzer)
    return retorno 
def totalarcos(analyzer):
    retorno = model.TotalDeArcos(analyzer)
    return retorno
def totalvertices(analyzer):
    retorno = model.TotalDeVertices(analyzer)
    return retorno 
def clusterentredosID(analyzer,id1,id2):
    retorno = model.ClusterPresence(analyzer,id1,id2)
    return 
def ensayo(analyzer):
    return model.ensayo(analyzer)
