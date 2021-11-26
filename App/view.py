﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from prettytable import PrettyTable

sys.setrecursionlimit(20000)

def print_aeropuerto(author):
    """
    Imprime la información del autor seleccionado
    """
    if author == '':
        print('No se encontraron artistas nacidos en el rango dado')
    elif author:
        print("\n")
        x = PrettyTable(["Nombre", "Ciudad", 'Pais','Latitud','Longitud'])
        x._max_width = {"Nombre" : 20, "Ciudad" : 20,"Pais" : 20, "Latitud" : 20,"Longitud" : 20}
        x.add_row([author['Name']+'\n', author['City'], author['Country'],author['Latitude'],author['Longitude']])
        print(x)
        print("\n")
    else:
        print('No se encontro el autor.\n')

def print_ciudades(author):
    """
    Imprime la información del autor seleccionado
    """
    if author == '':
        print('No se encontraron artistas nacidos en el rango dado')
    elif author:
        print("\n")
        x = PrettyTable(["Nombre", "Poblacion", 'Latitud','Longitud'])
        x._max_width = {"Nombre" : 20, "Poblacion" : 20,"Latitud" : 20, "Longitud" : 20}
        x.add_row([author['city']+'\n', author['population'], author['lat'],author['lng']])
        print(x)
        print("\n")
    else:
        print('No se encontro el autor.\n')

def print_opciones(author):
    """
    Imprime la información del autor seleccionado
    """
    if author:
        print("\n")
        x = PrettyTable(["Opcion","Ciudad", "Pais",'Admin','Latitud','Longitud'])
        x._max_width = {"Opcion" : 20,"Ciudad" : 20, "Pais" : 20, "Admin" : 20,"Latitud" : 20,"Longitud" : 20}
        numero = 1
        for artistas in lt.iterator(me.getValue(author)['repetidas']):
            x.add_row([numero, artistas['city'],artistas['country'],artistas['admin_name'],artistas['lat'],artistas['lng']])
            numero += 1
        print(x)
        print("\n")
    else:
        print('No se encontro el autor.\n')

def print_ciudades_opciones(author):
    """
    Imprime la información del autor seleccionado
    """
    if author == '':
        print('No se encontraron artistas nacidos en el rango dado')
    elif author:
        print("\n")
        x = PrettyTable(["Nombre","Pais","Admin","Poblacion", 'Latitud','Longitud'])
        x._max_width = {"Nombre" : 20,"Pais" : 20,"Admin" : 20, "Poblacion" : 20,"Latitud" : 20, "Longitud" : 20}
        x.add_row([author['city']+'\n', author['country'],author['admin_name'],author['population'], author['lat'],author['lng']])
        print(x)
        print("\n")
    else:
        print('No se encontro el autor.\n')


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de archivos de vuelos")
    print("3- Encontrar puntos de interconexión aérea")
    print("4- Encontrar clústeres de tráfico aéreo")
    print("5- ----------------ADELANTO REQUERIMIENTO TRES---------")
    print("6- Utilizar las millas de viajero")
    print("7- Cuantificar el efecto de un aeropuerto cerrado")
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print("Cargando información de los archivos ....")
        cont = controller.init()

    elif int(inputs[0]) == 2:

        controller.loadAirportsRutes(cont)
        print('\n' +('-'*20)+ 'Informacion grafo dirigido' +('-'*20)+ '\n')
        print('Numero de aeropuertos: ' + str(gr.numVertices(cont['rutas'])))
        print('Numero de rutas: ' + str(gr.numEdges(cont['rutas'])))
        print('\n' + 'Primer aeropuerto del grafo' + '\n')
        print_aeropuerto(controller.infoaeropuerto(cont,lt.firstElement(gr.vertices(cont['rutas']))))

        print('\n' +('-'*20)+ 'Informacion grafo no dirigido' +('-'*20)+ '\n')
        print('Numero de aeropuertos: ' + str(gr.numVertices(cont['rutas_idayretorno'])))
        print('Numero de rutas: ' + str(gr.numEdges(cont['rutas_idayretorno'])))
        print('\n' + 'Primer aeropuerto del grafo' + '\n')
        print_aeropuerto(controller.infoaeropuerto(cont,lt.firstElement(gr.vertices(cont['rutas_idayretorno']))))

        print('\n' +('-'*20)+ 'Informacion grafo dirigido solo con una direccion y sin repeticion' +('-'*20)+ '\n')
        print('Numero de aeropuertos: ' + str(gr.numVertices(cont['rutasconaerolineas'])))
        print('Numero de rutas: ' + str(gr.numEdges(cont['rutasconaerolineas'])))
        print('\n' + 'Primer aeropuerto del grafo' + '\n')
        print_aeropuerto(controller.infoaeropuerto(cont,lt.firstElement(gr.vertices(cont['rutasconaerolineas']))))

        print('\n' +('-'*20)+ 'Informacion ciudades' +('-'*20)+ '\n')
        print('Total de ciudades: ' + str(lt.size(cont['ciudades'])))
        print('\n' + 'Ultima ciudad cargada' + '\n')
        print_ciudades(lt.lastElement(cont['ciudades']))

        print('\n' + 'Primer aeropuerto del archivo' + '\n')
        print_aeropuerto(lt.firstElement(cont['aeropuertosinfolista']))

    elif int(inputs[0]) == 3:

        respuesta = controller.primer_req(cont)
        print('aqui se ve a presentar la lista de areopuertos y el numero de aeropuertos conectados del grafo dirigido')
        print('\n' + 'El numero de aeropuertos conectados es de:' + str(respuesta[0]))
        print_aeropuerto(respuesta[1])

        print('aqui se ve a presentar la lista de areopuertos y el numero de aeropuertos conectados del grafo no dirigido')
        print('\n' + 'El numero de aeropuertos conectados es de:' + str(respuesta[2]))
        print_aeropuerto(respuesta[3])

    elif int(inputs[0]) == 4:
        
        print('aqui se ve a presentar el cluster prsente en la red de aeropuertos y una comparacion')
        codigo1 = input('Escriba el codigo del primer aeropuerto')
        codigo2 = input('Escriba el codigo del segundo aeropuerto')
        respuesta = controller.segundo_req(cont,codigo1,codigo2)
        print('\n' + 'El numero de elementos fuertemente conectados es de:' + str(respuesta[0]))
        print('\n' + 'Los dos vertices estan fuertemente conectados:' + str(respuesta[1]))

    elif int(inputs[0]) == 5:
        
        print('aqui se ve a presentar lla ruta mas corta entre dos ciudades')
#ORIGEN -------------------------------------------------------------------------------------------------
        ciudad1 = input('Escriba el nombre de la ciudad de origen')
        opcion_origen = controller.opciones_ciudades(cont,ciudad1)
        print_opciones(opcion_origen)
        ciudad_origen = input('Escriba la opcion de la tabla de arriba que desea buscar')
        info_ciudad_origen = lt.getElement(me.getValue(opcion_origen)['repetidas'],int(ciudad_origen))
        print_ciudades_opciones(info_ciudad_origen)
        aeropuerto1 = controller.aeropuertoopciones(cont,info_ciudad_origen)
        print('\n' + 'El aeropuerto de salida seleccionado es:' + str(aeropuerto1['aeropuerto']))

#DESTINO-------------------------------------------------------------------------------------------------
        ciudad2 = input('Escriba el nombre de la ciudad de destino')
        opcion_destino = controller.opciones_ciudades(cont,ciudad2)
        print_opciones(opcion_destino)
        ciudad_destino = input('Escriba la opcion de la tabla de arriba que desea buscar')
        info_ciudad_destino = lt.getElement(me.getValue(opcion_destino)['repetidas'],int(ciudad_destino))
        print_ciudades_opciones(info_ciudad_destino)
        aeropuerto2 = controller.aeropuertoopciones(cont,info_ciudad_destino)
        print('\n' + 'El aeropuerto de destino seleccionado es:' + str(aeropuerto2['aeropuerto']))

    elif int(inputs[0]) == 6:
        
        print('aqui se ve a presentar la red expansion minima')

    elif int(inputs[0]) == 7:
        
        print('aqui se ve a presentar la afectacion de un vuelo')

    else:
        sys.exit(0)
sys.exit(0)
