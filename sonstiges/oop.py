class Microwave:
    def __init__(self, brand:str, power_rating:str) -> None:
        self.brand = brand
        self.power_rating = power_rating


# type annotation
smeg: Microwave = Microwave("Smeg", "B")
print(smeg.brand + smeg.power_rating)
bosch = Microwave("bosch", "A")
print(bosch.brand + bosch.power_rating)
