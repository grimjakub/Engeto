TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
         red, purple, yellow and gray beds of the Wasatch 
         Formation. Eroded portions of these horizontal 
         beds slope gradually upward from the valley floor 
         and steepen abruptly. Overlying them and extending 
         to the top of the butte are the much steeper 
         buff-to-white beds of the Green River Formation, 
         which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
         a portion of the largest deposit of freshwater fish 
         fossils in the world. The richest fossil fish deposits 
         are found in multiple limestone layers, which lie some 
         100 feet below the top of the butte. The fossils 
         represent several varieties of perch, as well as 
         other freshwater genera and herring similar to those 
         in modern oceans. Other fish such as paddlefish, 
         garpike and stingray are also present.'''
         ]

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}  # registrovani uzivatele
pocet_oddelovacu = 30  # kolik tam chci oddelovacich carek

username = input("username: ")
if username in users.keys():
    print("Username already exists!\n---EXIT---")
    exit()
elif username == "":
    print("You must use a username!\n---EXIT---")
    exit()
password = input("password: ")
if password == "":
    print("You must use a password!\n---EXIT---")
    exit()

print("-" * pocet_oddelovacu)
print(f"Welcome to the app, {username}\nWe have {len(TEXTS)} texts to be analyzed.")
print("-" * pocet_oddelovacu)

index = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")  # ptam se na text ktery chce uzivatel vybrat
if not index.isnumeric():
    print("Not a number!\n---EXIT---")
    exit()
elif int(index) > len(TEXTS):
    print("This number is not in range!\n---EXIT---")
    exit()
print("-" * pocet_oddelovacu)

index = int(index) - 1  # indexuju od 0, ne od 1
pocet_slov = len(TEXTS[index].split())
zacina_velkym = 0
velka_pismena = 0
mala_pismena = 0
pocet_cisel = 0
soucet_cisel = 0
pocitani_delky_slov = {}

for slovo in TEXTS[index].split():
    slovo = slovo.strip(".,")
    if slovo.istitle():
        zacina_velkym += 1
    elif slovo.isupper():
        velka_pismena += 1
    elif slovo.islower():
        mala_pismena += 1
    elif slovo.isnumeric():
        pocet_cisel += 1
        soucet_cisel += int(slovo)
    pocitani_delky_slov[len(slovo)] = pocitani_delky_slov.get(len(slovo), 0) + 1

print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {zacina_velkym} titlecase words.")
print(f"There are {velka_pismena} uppercase words.")
print(f"There are {mala_pismena} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {soucet_cisel}")
print("-" * pocet_oddelovacu)

max_val = max(pocitani_delky_slov.values())
print("LEN|" + " " * (max_val - 11) + "OCCURENCES  |NR.")
print("-" * pocet_oddelovacu)

for key, val in sorted(pocitani_delky_slov.items()):
    if key < 10:    #abych vse zarovnal pod sebe
        print(" ", end="")
    print(key, "|" + "*" * val + " " * (max_val - val), "|", val)
