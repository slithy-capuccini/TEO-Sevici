from bikes import *

def main():
    stations=read_stations("./data/estaciones.csv")
    print(f"First three stations: {stations[0:3]}")
    print(free_bikes_stations(stations, 22))
    print(f"Estas son las estaciones con más de las bicis indicadas")
    print(near_stations(stations, Coordinates(37.357659,-5.9863)))  
    print(avarage_coord(stations))
    my_map=create_map(stations,lambda s:"blue")
    save_map(my_map, "./out/blue.html")
if __name__ =="__main__":

    main()