path = "bundeslaender.csv"
new_file_path = "bundeslaender_new.csv"

def calc_inhabitants_per_qkm(inhabitants:int, area:int) -> int:
    return inhabitants / area

def writedata(datei_path, data):
    with open(datei_path, "a") as file:
        file.write(data)

with open(path, "r") as file:
    csv = file.read().split("\n")
    index = 0
    for line in csv:
        index += 1
        row = line.split(",")
        inhabitants = row[2]
        area = row[1]
        if index > 1:
            inhabitants = int(inhabitants)
            area = int(area)
            inhabitants_per_qkm = calc_inhabitants_per_qkm(inhabitants=int(inhabitants), area=int(area))
            row.append(inhabitants_per_qkm)
            writedata(new_file_path, f"{row}\n")

