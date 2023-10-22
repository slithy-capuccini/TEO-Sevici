import csv
from collections import namedtuple
import math
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

def avarage_coord(stations):
    #devuelve una cordenada que es la media de las longitudes y otra de las latitudes
    avr_latitudes=sum([i.location.latitude for i in stations])/len(stations)
    avr_longitudes=sum([i.location.longitude for i in stations])/len(stations)
    return avr_latitudes, avr_longitudes
