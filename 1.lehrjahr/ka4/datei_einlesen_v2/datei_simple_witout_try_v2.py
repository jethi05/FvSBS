path = "bundeslaender.csv"
new_file_path = "bundeslaender_new.csv"


def writedata(datei_path, data) -> None:
    with open(datei_path, "a") as file:
        file.write(f"{data}\n")

def add_header(datei_path:str, header:str) -> None:
    with open(datei_path, "w") as file:
        file.write(header)
    

def calc_inhabitants_per_qkm(inhabitants:float, area:float) -> float:
    return inhabitants / area


def calc_population_density(inhabitants:float, area:float) -> float:
    return inhabitants / area

def add_to_total_area(data:float, total_area:float) -> float:
    return total_area + data

def add_to_total_population(data:float, total_population:float) -> float:
    return total_population + data

def calc_anteil_gesamtflaeche(area:float) -> float:
    return total_area / area

def calc_anteil_gesamtbevoelkerung(inhabitants:float) -> float:
    return total_population / inhabitants



with open(path, "r") as file:
    csv = file.read().split("\n")
    index = 0
    total_area = 0
    total_population = 0
    for line in csv:
        index += 1
        row = line.split(",")
        inhabitants = row[2]
        area = row[1]
        bundesland = row[0]
        if index > 1:
            inhabitants = float(inhabitants)
            area = float(area)

            total_area = add_to_total_area(area, total_area=total_area) #Fuege daten zu den total var hinzu
            total_population = add_to_total_population(inhabitants, total_population=total_population) #Fuege daten zu den total var hinzu

            inhabitants_per_qkm = calc_inhabitants_per_qkm(inhabitants=float(inhabitants), area=float(area))
            population_density = calc_population_density(inhabitants=float(inhabitants), area=float(area))
            flaechenanteil= calc_anteil_gesamtflaeche(area=float(area))
            bevoelkerungsanteil = calc_anteil_gesamtbevoelkerung(inhabitants=float(inhabitants))

            new_row = f"{bundesland}, {area}, {inhabitants:.2f}, {inhabitants_per_qkm:.2f}, {population_density:.2f}, {flaechenanteil:.2f}, {bevoelkerungsanteil:.2f}"

            writedata(new_file_path, new_row)
        else:
            headers = "Bundesland, Flaeche, Einwohner, Einwohner je qkm, Bevoelkerungsdichte, Anteil an Gesamtflaeche, Anteil an Gesamtbevoelkerung\n"
            add_header(new_file_path, header=headers)
    


    


        

