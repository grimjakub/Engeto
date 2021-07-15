oddelovac = "=" * 40

print("Welcome to Tic Tac Toe")
print(oddelovac)
print("""             GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row""")
print(oddelovac)
print("          Let's start the game")
print("-" * 40)

p = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def round(x):
    while True:
        try:
            print(oddelovac)
            player=int(input(f"Player {x} | Please enter your move number: "))
            print(oddelovac)
        except:
            print("please enter number")
            continue
        if player>9:
            print("too much")
            continue
        elif p[player-1]!=" ":
            print("obsazeno")
            continue

        break
    p[player-1]=x

    print(f"""             +---+---+---+
             | {p[0]} | {p[1]} | {p[2]} |
             +---+---+---+
             | {p[3]} | {p[4]} | {p[5]} |
             +---+---+---+
             | {p[6]} | {p[7]} | {p[8]} |
             +---+---+---+
    """)

while True:
    round("o")
    False
    round("x")
    break
