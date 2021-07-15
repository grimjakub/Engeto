import random

oddelovac = "-" * 47
tajne_cislo = random.randrange(1000, 10000)
print("Tajné číslo:", tajne_cislo)  # pak smazat!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(oddelovac)
try:
    pokus = int(input("Enter a number: "))
except ValueError:
    print("blbec")
