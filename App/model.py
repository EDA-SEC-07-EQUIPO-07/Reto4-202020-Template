import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

# -----------------------------------------------------
#                       API
def analyzer():
    analyzer = {"indice":None,
                "grafo":None}
    analyzer["indice"] = m.newMap(numelements=1000, 
                                  prime=109345121, 
                                  maptype="CHAINING",
                                  loadfactor=1.0, 
                                  comparefunction=None)      

    analyzer["grafo"] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=1000,
                                  comparefunction=comparer)
    return analyzer

# -----------------------------------------------------
# Funciones para agregar informacion al grafo
def AñadirRuta(analyzer, route):
    """
    """
    origin = route['start station id']
    destination = route['end station id']
    duration = int(route['tripduration'])
    AñadirEstacion(analyzer, origin)
    AñadirEstacion(analyzer, destination)
    AñadirConeccion(analyzer, origin, destination, duration)

def  AñadirEstacion(analyzer, estacion):
    if not gr.containsVertex(analyzer["grafo"], estacion):
        gr.insertVertex(analyzer["grafo"], estacion)
    return analyzer

def AñadirConeccion(analyzer, origin, destination, duration):
    edge = gr.getEdge(analyzer["grafo"], origin, destination)
    if edge is None:
        gr.addEdge(analyzer["grafo"], origin, destination, duration)
    else:
        edge["weight"] = (edge["weight"]+int(duration))/2
    return analyzer

# ==============================
# Funciones de consulta
# ==============================
def TotaldeClusteres(analyzer):
    i = scc.KosarajuSCC(analyzer["grafo"])
    retorno = scc.connectedComponents(i)
    return retorno

def ClusterPresence(analyzer,id1,id2):
    i = scc.KosarajuSCC(analyzer["grafo"])
    retorno = scc.stronglyConnected(i, id1, id2)
    return retorno

def TotalDeVertices(analyzer):
    retorno = gr.numVertices(analyzer["grafo"])
    return retorno

def TotalDeArcos(analyzer):
    retorno = gr.numEdges(analyzer["grafo"])
    return retorno

# ==============================
# Funciones de Comparacion
# ==============================
def comparer(stop, keyvaluestop):
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1
