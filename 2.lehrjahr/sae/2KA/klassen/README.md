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

gekapselte Attribute == zwei Unterstriche?
set = gibt was ein
get = gibt was aus

Convention |  Example     |  Meaning
------------|-------------|------------
Single leading underscore  | _variable  | Indicates that the name is meant for internal use only
Single trailing underscore | class_  | Avoids naming conflicts with Python keywords and built-in names
Double leading underscore  |  __attribute |    Triggers name mangling in the context of Python classes
Double leading and trailing underscore  | __name__  |  Indicates special attributes and methods that Python provides
Single underscore |  _  | Indicates a temporary or throwaway variable
