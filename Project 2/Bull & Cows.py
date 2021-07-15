import random

oddelovac = "-" * 47
while True:
    tajne_cislo = random.randrange(1000, 10000)
    cislo_list = [int(s) for s in str(tajne_cislo)]
    if sorted(cislo_list) == sorted(set(cislo_list)):
        break

print("Tajné číslo:", tajne_cislo)  # pak smazat!
print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(oddelovac)
print("Enter a number: ")

pocet_pokusu = 0
while True:
    print(oddelovac)
    pokus = (input())
    if len(pokus) != 4 or not pokus.isdigit():
        print("Must be 4-digit number")
        continue
    if pokus[0] == "0":
        print("0 can not be first digit")
        continue
    pokus_list = [int(s) for s in str(pokus)]
    if sorted(pokus_list) != sorted(set(pokus_list)):
        print("No duplicated digits")
        continue
    pocet_pokusu += 1
    bull = 0
    cow = 0
    for i in range(4):
        if pokus_list[i] == cislo_list[i]:
            bull += 1
        elif pokus_list[i] in cislo_list:
            cow += 1
    if bull == 4:
        print(f"Correct, you've guessed the right number\nin {pocet_pokusu} guesses!")
        break
    else:
        bull_str = "bull" if bull == 1 else "bulls"
        cow_str = "cow" if cow == 1 else "cows"
        print(f"{bull} {bull_str}, {cow} {cow_str}")
print(oddelovac)
print("Thats's amazing")

## Zápis historie jednotlivých her
# with open("game_logs.txt","a") as file:
#     file.writelines(f"pocet_pokusu: {pocet_pokusu}\n")
