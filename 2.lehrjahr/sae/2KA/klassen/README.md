# Klassen
Beispiel Stifte  
**Klassen** werden immer in `CammelCase` geschrieben  
```{python}
class Stift:
```
**`__init__`** ist ein **Konstruktor**, dadruch werden die Startwerte gesetzt.  
**`self`** ist eine Selbstreferenz, wie "Ich" in der Sprache  
`Attribut == Variable`  
```{python}
def __init::(self, farbe):
    self.farbe = farbe
```
In jeder weiteren Funktion muss weiterhin self mitgegeben werden:
```{python}
def schreibe(self, text):
    print(f"{self.farbe}-farbender Stift schreibt {text}")
```
Danach kann dies folgender maßen aufgerufen werden
```{python}
rotstift = Stift("rot")
rotstift.schreibe("Hallo Klasse")

## Aufgabe 2
```
class Tier:                                                                     
     def __init__(self, laut):                                                   
         self.laut = laut                                                        
     def gib_laut(self):                                                         
         print(f"Tier gibt laut {self.laut}")                                    
hund = Tier("Wuff")                                                             
hund.gib_laut()                                                                 
katze = Tier("Miau")                                                            
katze.gib_laut()
```

Katze kann auch "Gehackt" werden, indem auf die Variable zugegriffen wird
```

print(katze.laut)
katze.laut= "Quieck"
katze.gib_laut()
```

