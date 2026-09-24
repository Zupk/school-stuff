def game(igra:list):
    while True:
        p1 = input("Vnos prvega igralca: ")
        p2 = input("Vnos drugega igralca: ")
        if p1 == "" or p2 == "":
            break
        igra.append(p1)
        igra.append(p2)

def rez(igra:list):
    spr1 = 0
    spr2 = 1
    rezultat = []
    for index in range(len(igra)):
        if igra[spr1] == "k" and igra[spr2] == "s":
            rezultat.append("P1")
        elif igra[spr1] == "k" and igra[spr2] == "p":
            rezultat.append("P2")
        elif igra[spr1] == "s" and igra[spr2] == "k":
            rezultat.append("P2")





if __name__ == "__main__":
    igra = []
    game(igra)
    rez(igra)