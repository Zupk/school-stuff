def game(igra:list):
    while True:
        p1 = input("Vnos prvega igralca: ")
        p2 = input("Vnos drugega igralca: ")
        if p1 == "" or p2 == "":
            break
        igra.append(p1)
        igra.append(p2)

def rez(igra:list, rezultat:list):
    spr1 = 0
    spr2 = 1
    for index in range((len(igra))//2):
        if igra[spr1] == "k" and igra[spr2] == "s":
            rezultat.append("P1")
            spr1 += 2
            spr2 += 2
        elif igra[spr1] == "k" and igra[spr2] == "p":
            rezultat.append("P2")
            spr1 += 2
            spr2 += 2
        elif igra[spr1] == "s" and igra[spr2] == "k":
            rezultat.append("P2")
            spr1 += 2
            spr2 += 2
        elif igra[spr1] == "s" and igra[spr2] == "p":
            rezultat.append("P1")
            spr1 += 2
            spr2 += 2
        elif igra[spr1] == "p" and igra[spr2] == "k":
            rezultat.append("P1")
            spr1 += 2
            spr2 += 2
        elif igra[spr1] == "p" and igra[spr2] == "s":
            rezultat.append("P2")
            spr1 += 2
            spr2 += 2
        elif igra[spr1] == igra[spr2]:
            spr1 += 2
            spr2 += 2
    print(rezultat)
    return rezultat

def zmaga(rezultat:list):
    z1 = 0
    z2 = 0
    zmagovalec = []
    for index in range(len(rezultat)):
        if rezultat[index] == "P1":
            z1 += 1
        elif rezultat[index] == "P2":
            z2 += 1
    zmagovalec.append(z1)
    zmagovalec.append(z2)
    print(zmagovalec)



if __name__ == "__main__":
    igra = []
    rezultat = []
    game(igra)
    rez(igra, rezultat)
    zmaga(rezultat)