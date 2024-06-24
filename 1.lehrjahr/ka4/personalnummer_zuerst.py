'''Programm um Die Personalnummer als erstes anzuzeigen'''
neue_liste=[]
wirth = [
    "Mueller|Josef|FR_1112|Freiburg",
    "Maier|Fritz|ST_1114|Vaihingen",
    "Heinze|Maria|ST_5525|Bad Cannstatt",
    "Herrman|Georg|FR_2536|Merzhausen",
    ]
schneider = [
    "Schneider|Wolfgang|Heidelberg|HE_20011",
    "Bartels|Martina|Sandhausen|HE_15436",
    "Beck|Hans|Neckarsteinach|HE_5436",
    ]
def fof(listenname, sep):
    '''Personalnummer zuerst hinschreiben'''
    for line in listenname:
        splited_line = line.split("|")
        splited_line.insert(0, splited_line[sep])
        splited_line.pop(sep + 1)
        string=" ".join(splited_line)
        neue_liste.append(string)
    return neue_liste
print(fof(wirth, 2))
print(fof(schneider, 3))
