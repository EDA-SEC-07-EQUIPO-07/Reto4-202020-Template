import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config

# ___________________________________________________
#  Menu principal
def Menu():
    print("\n")
    print("Bienvenido")
    print("1- Iniciar el catalogo")
    print("2- Cargar archivos al catalogo")
    print("3- Cantidad de clusters en el grafo")
    print("0- Salir")

# ___________________________________________________
archivo = "201801-1-citibike-tripdata.csv"
def option_three(analyzer):
    id1 = input("ID de la primera estación: ")
    id2 = input("ID de la segunda estacion: ")
    total = controller.totalClusters(analyzer)
    haycluster = controller.clusterentredosID(analyzer,id1,id2)
    print("Total clústeres: ",total)
    if haycluster==True:
        print("Si hay componentes fuertemente conectados entre la id: "+id1+" y la id: "+id2)
        print(analyzer["grafo"])
    else:
        print("No hay componentes fuertemente conectados entre las ids")
def OpcionesMenu():
    analyzer = None
    i = True
    while i == True:
        Menu()
        opciones = str(input("Seleccione una opción:"))
        if opciones == "1":
            analyzer = controller.InitCatalog()
            if analyzer != None:  
                print("Catalogo creado") 
            else:
                print("Error al cargar el catalogo")
        elif opciones == "2":
            Datos = controller.loadTrips(analyzer, archivo)
            print("\n") 
            print(Datos[0])
            print(Datos[1])
            print(Datos[2])
        elif opciones == "3":
            option_three(analyzer)
        elif opciones == "0":
            i = False
OpcionesMenu()
