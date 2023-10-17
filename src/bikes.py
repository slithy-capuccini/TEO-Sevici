import csv
from collections import namedtuple

Coordinates=namedtuple("Coordinates","latitude, longitude")
Station=namedtuple("Station","name, slots, empty_slots, free_bikes, location")

def read_stations(file):
    #open file
    #create a csv reader
    #skip the first line
    #read the content of the file and create a list of tuples of type station
    with open(file) as f:
        
        lector=csv.reader(f)
        next
        auds_md=[(name, int(slots),int(empty),int(free),float(latitude),float(longitue)) for name, slots,empty,free,latitude,longitue in lector]#take edition of the program and share of the program with comprehension
        print(auds_md)
    