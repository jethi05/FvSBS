#! usr/bin/python3
# zahln von 1 bis 100 ausgeben fizz wenn modolo 3 buzz wenn 5

x = 0
while x <= 100:
    if x%3 == 0:
        ausgabe = "fizz"
    if x%5 ==0:
        ausgabe += " buzz"
    print(ausgabe)
    x += 1
