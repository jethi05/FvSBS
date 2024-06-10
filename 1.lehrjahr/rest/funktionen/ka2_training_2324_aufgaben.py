# 1. Forme sämtliche while-Übungen in Funktionen um.

# 2.
# Reutlingen ist berühmt für seine Wintermode, gesunden Bürger und exkuisiten Speisen.
# Die wertvollen Felle, Omega-3-Fette und Filets müssen aber erst mit viel Mühe aus den Robben in den Echazauen herausgeholt werden.
# Reutlinger Geschäftsleute scheuen diese Mühen nicht und jagen jedes Jahr genug Graue Echazrobben, damit ihre Kunden glücklich und zufrieden sind.
# Die Population der Grauen Echazrobbe sinkt jedes Jahr auf drei Viertel des Vorjahresbestands. Derzeit gibt es 740 Individuen.
# Da Reutlingen auch für seine Nachhaltigkeit berühmt ist, möchte es die Robbe erhalten. Du erhältst folgenden Auftrag der Robbenjägerei-Innung:
# 2 a)
# Schreibe eine Funktion, die die Anzahl der Individuen als Parameter bekommt und die Anzahl der Jahre berechnet, bis noch zwei Echazrobben übrig sind.des
# Vorjahres).
# 

#po 3/4 des Vorjahres =740

def robbidobbi(robben):
    while robben >=2:
        print(f"Geradige Robben: {robben}")
        robben = robben *0.75
#robbidobbi(740)




#2 b)
# Schreibe die Funktion so allgemein, dass sie auch für den Achalmfuchs (Population von 12, sinkt jährlich auf die Hälfte, wird bis
# zu drei Individuen gejagt) angewendet werden kann.


def allgemeine_funktion(pop,end_pop, proz):
    while pop > end_pop:
        pop = pop * proz
        print(pop)




#3
# Jede Erzieherin in einer bayrischen Kita betreut 4 Kinder (Betreuungschlüssel = 4). Im Ort Kuhflading gibt es derzeit 40 Kinder und entsprechend 10 Erzieherinnen.
# Jedes Jahr werden mehr Kinder geboren. Die Wachstumsrate der Bevölkerung durch Geburten liegt voraussichtlich noch sehr lange stabil bei 5% (* 0.05).
# Schreibe eine Funktion die berechnet, in wie vielen Jahren sich die Anzahl der Erzieherinnen verdoppelt hat.
# Übergabeparameter: Anzahl Kinder, Wachstumsrate, Betreuungschluessel
# Beispiel: Für den Ort Facking mit (Kinder: 100, Wachstumsrate = 0.10, Betreuungschlüssel: 4) wäre das Ergebnis 8 Jahre.

def kindergarten(anz_kinder, wachstum, betr_schluessl):
    jahre = 0
    anz_erziehr = betr_schluessl*wachstum
    while_anz_erz = anz_erziehr
    while anz_erziehr*2 > while_anz_erz:
        anz_kinder = anz_kinder*wachstum
        while_anz_erz = betr_schluessl/anz_kinder
        print(while_anz_erz)
        jahre += 1
        print(jahre)
#kindergarten(100, 0.18, 4)
        





#4
# Du entwickelst eine App zur Reiseplanung.

# 4 a)
# Schreibe eine Funktion, die eine Geschwindigkeitsangabe in km/h nach folgenden Kriterien klassifiziert und die Klassifikation als
# String zurückliefert.
# Unter 100 km/h:
#     „Du fährst sehr langsam.“
# 100 bis 130 km/h:
#     „Du fährst mit der idealen Geschwindigkeit.“
# Über 130 km/h:
#     „Du fährst zu schnell!“


# dies ist eine If Aufgabe, ich mache die ihnen im Kopf



# 4 b)
# Schreibe eine Funktion, Distanz, Geschwindigkeit und Pausenzeit übergeben bekommt
# und die Reisedauer in Stunden zurückgibt. Diese wird wie folgt berechnet:
# reisedauer = distanz/geschwindigkeit + pausenzeit/60


def reisedauer(dist, geschw, pause):
    zeit = dist/geschw + pause/60
    print(zeit)

# 4 c)
# Schreibe eine Funktion, Distanz, Geschwindigkeit und Pausenzeit über die Tastatur
# einliest und die Funktionen aus 4 a) und 4 b) benutzt um sowohl die Klassifikation auf der Konsole auszugeben
# als auch die Reisedauer zu berechnen.


def reise(dist, geschw, pause):
    if geschw > 100:
        print("DU fährst du langsam")
    elif geschw < 130:
        print("DU fährst die ideale Geschwindigkeit")
    else:
        print("Du fährat zu schnell")
    zeit = dist/geschw + pause/60
    print(zeit)

#reise(100, 100, 60)








