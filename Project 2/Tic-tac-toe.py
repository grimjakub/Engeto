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

# pocatecni stav hry
p = [" ", " ", " ",
     " ", " ", " ",
     " ", " ", " "]


def round(x):
    while True:
        try:
            print(oddelovac)
            move = int(input(f"Player {x} | Please enter your move number: "))
            print(oddelovac)
        except:
            print("Please enter a number")
            continue
        if move > 9:
            print("too much")
            continue
        elif p[move - 1] != " ":
            print("obsazeno")
            continue
        break
    p[move - 1] = x
    gameStatus()


def gameStatus():
    print(f"""             +---+---+---+
             | {p[0]} | {p[1]} | {p[2]} |
             +---+---+---+
             | {p[3]} | {p[4]} | {p[5]} |
             +---+---+---+
             | {p[6]} | {p[7]} | {p[8]} |
             +---+---+---+
    """)


def checkWinner(player):
    if p[0] == p[1] == p[2] != " " or p[3] == p[4] == p[5] != " " or p[6] == p[7] == p[8] != " " or p[0] == p[4] == p[
        8] != " " or p[2] == p[4] == \
            p[6] != " " or p[0] == p[3] == p[6] != " " or p[1] == p[4] == p[7] != " " or p[2] == p[5] == p[8] != " ":
        print(f"Congratulations, the player {player} WON!")
        return True
    elif " " not in p:
        print("Sorry, nobody wins")
        return True
    return False


# GAME
while True:
    for player in ["o", "x"]:
        round(player)
        if checkWinner(player):
            break
