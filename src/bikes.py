import csv
from collections import namedtuple

Coordinates=namedtuple("Coordinates","latitude, longitude")
Station=namedtuple("Station","name, slots, empty_slots, free_bikes, location")

def read_stations(file):
    encodings_to_try = ['utf-8', 'latin-1', 'cp1252', 'utf-16']

    for encoding in encodings_to_try:
        try:
            with open(file, 'r', encoding=encoding) as csv_file:
                csv_reader = csv.reader(csv_file)
                lista=[]            
                next(csv_reader)    
                for name,slots,empty_slots,free_bikes,latitude,longitude in csv_reader:
                    slots=int(slots)
                    empty_slots=int(empty_slots)
                    free_bikes=int(free_bikes)
                    location=Coordinates(latitude,longitude)
                    lista.append(Station(name,slots,empty_slots,free_bikes,location))    
                
                return lista
            break  # If successful, stop trying other encodings
        except UnicodeDecodeError:
            continue  # If an error occurs, try the next encoding

