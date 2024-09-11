#!/usr/bin/python3
'''Dieses Programm ist dafür da, um sitemap.txt neu zu gestalten, da einige Links zu alt sind'''
def change_domain(string):
    string = string.replace("holzschule", "holzschule-calw")
    return string

def change_stupla(string):
    string = string.replace("stupla", "stundenplan")
    return string

def change_ausflg(string):
    string = string.replace("ausflg", "exkursion")
    return string

def change_jpg(string):
    string = string.replace("jpg", "pdf",-1)
    return string

def change_path(string):
    if "news" in string:
        string = string.replace("/news", "")
        string = string.replace("www.holzschule-calw.de/main", "")
        string = "www.holzschule-calw.de/main/news" + string
    return string

with open("sitemap.txt", "r", encoding="utf8") as file:
    lines = file.readlines()
with open("sitemap_neu.txt", "w", encoding="utf8") as new_file:
    for line in lines:
        line = change_domain(line)
        line = change_stupla(line)
        line = change_jpg(line)
        line = change_path(line)
        new_file.write(line)
print("Done")

''' Also jetzt mal ganz ehrlich, welcher Idiot würde das so lösen?
Ich habe selten so einen scheiß gesehen... man hätte auch nur eine Funktion
machen können...'''
