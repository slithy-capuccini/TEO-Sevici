import csv
from collections import namedtuple
import math
import folium
import webbrowser
import os
Coordinates=namedtuple("Coordinates","latitude, longitude")
Station=namedtuple("Station","name, slots, empty_slots, free_bikes, location")

def read_stations(file):
    with open(file, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        lista=[]            
        next(csv_reader)    
        for name,slots,empty_slots,free_bikes,latitude,longitude in csv_reader:
            slots=int(slots)
            empty_slots=int(empty_slots)
            free_bikes=int(free_bikes)
            location=Coordinates(float(latitude),float(longitude))
            lista.append(Station(name,slots,empty_slots,free_bikes,location))    
        
        return lista

def free_bikes_stations(stations, k=5):
    #list of tuples of stations with more than k bikes
    return sorted([[i.free_bikes,i.name] for i in stations if i.free_bikes>=k], reverse=False)#we want to sort by first the smaller elements

def calcula_distancia(coord1,coord2):
    return math.sqrt((coord2.latitude-coord1.latitude)**2+(coord2.longitude-coord1.longitude)**2)

def near_stations(stations,coord,k=5):
    lista_distancias=[]
    for i in range(len(stations)):
        lista_distancias.append([calcula_distancia(stations[i].location, coord),i])
    lista_distancias=sorted(lista_distancias, reverse=False)
    lista_out=[]
    for i in range(k):
        lista_out.append([stations[lista_distancias[i][1]].name, stations[lista_distancias[i][1]].free_bikes, lista_distancias[i][0]])
    return lista_out
def create_map(latitud, longitud, zoom=9):
    '''
    Función que crea un mapa folium que está centrado en la latitud y longitud
    dados como parámetro y mostrado con el nivel de zoom dado.
    ENTRADA:
        :param latitud: latitud del centro del mapa en pantalla
        :type latitud:float
        :param longitud: longitud del centro del mapa  en pantalla
        :type longitud: float
        :param zoom: nivel del zoom con el que se muestra el mapa
        :type zoom: int
    SALIDA:
        :return: objeto mapa creado
        :rtype: folium.Map
    '''
    mapa = folium.Map(location=[latitud, longitud], 
                      zoom_start=zoom)
    return mapa    
def save_map(mapa, ruta_fichero):
    '''Guard un mapa como archivo html

    :param mapa: Mapa a guardar
    :type mapa: folium.Map
    :param ruta_fichero: Nombre y ruta del fichero
    :type ruta_fichero: str
    '''
    mapa.save(ruta_fichero)
    # Abre el fichero creado en un navegador web
    webbrowser.open("file://" + os.path.realpath(ruta_fichero))
def avarage_coord(stations):
    #devuelve una cordenada que es la media de las longitudes y otra de las latitudes
    avr_latitudes=sum([i.location.latitude for i in stations])/len(stations)
    avr_longitudes=sum([i.location.longitude for i in stations])/len(stations)
    return avr_latitudes, avr_longitudes

def create_map_stations(stations, funcion_color):
    centro_mapa=avarage_coord(stations)
    mapa=create_map(centro_mapa.latitude,centro_mapa.longitude,13)
    for estacion in stations:
        etiqueta=estacion.nombre
        color=funcion_color(estacion)
