def pruefeNummer(kartennummer:list) -> bool:
    index = 0
    summe = 0
    for zahl in kartennummer:
        index += 1
        if index <= 9:
            summe += index * zahl
    return summe % 10 == kartennummer[9]

def pruefeNummer2(kartennummer:list) -> bool:
    index = 0
    summe = 0
    while index < 9:
        summe += (index + 1) * kartennummer[index]
        index += 1
    return summe % 10 == kartennummer[9]

def pruefeNummer3(kartennummer:list) -> bool:
    index = 0
    summe = 0
    for zahl in kartennummer[:9]:
        index += 1
        summe += index * zahl
    return summe % 10 == kartennummer[9]

print(pruefeNummer3([5,1,2,4,8,9,7,2,5,3]))


