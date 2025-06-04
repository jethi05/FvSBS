# Klassen immer CammelCase
class Stift:

    # __init__ ist ein Konstruktur, dadurch werden die Startwerte gesetzt
    # self ist eine Selbstreferenz -> wie "Ich" in der Sprache
    # Attribut == Variable
    def __init__(self, farbe):
        self.farbe = farbe

    def schreibe(self, text):
        print(f"{self.farbe}-farbender Stift schreibt {text}")

#rotstift = Stift("rot")
#rotstift.schreibe("Hallo Klasse")

class Tier:
    def __init__(self, laut):
        self.laut = laut

    def gib_laut(self):
        print(f"Tier gibt laut {self.laut}")
hund = Tier("Wuff")
hund.gib_laut()

katze = Tier("Miau")
katze.gib_laut()

# Katze hacken
print(katze.laut)
katze.laut: str = "Quieck"
katze.gib_laut()
