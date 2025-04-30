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
