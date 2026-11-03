def vaja1():
    doma = int(input("Vnesi število golov domačih: "))
    gostje = int(input("Vnesi število golov gostov: "))
    print(f"Domači: {doma}\nGostje: {gostje}\nPopravljen rezultat: {gostje}:{doma}\nSkupaj: {doma+gostje}")

def vaja2():
    vnos = int(input("Koliko minut si igral: "))
    ure = vnos // 60
    minu = vnos % 60
    dni = ure // 24
    ure = ure - 24*dni
    print(f"{dni} dni,{ure} ure,{minu} min")

def vaja3():
    dijaki = int(input("Koliko je dijakov: "))
    cena = float(input("Koliko stane ena pica: "))
    stPic = dijaki // 3
    if dijaki % 3 != 0:
        stPic += 1
    print(f"Skupaj: {stPic*cena} EUR\nNa dijaka: {round((stPic*cena)/dijaki, 2)} EUR")

def vaja4():
    starost = int(input("vnesi starost: "))
    dan = input("vnesi dan: ").lower()
    noDiscount = ["pondelk","sreda","cetrtek","petek","sobota","nedelja"]
    if dan == "torek":
        if starost < 0:
            print("neveljavna starost")
        elif 0 <= starost <= 5:
            print("brezplacni vhod")
        elif 6 <= starost <= 17:
            print("cena: 3 EUR")
        elif 18 <= starost <= 64:
            print("cena: 6 EUR")
        else:
            print("cena: 4 EUR")
    elif dan in noDiscount:
        if starost < 0:
            print("neveljavna starost")
        elif 0 <= starost <= 5:
            print("brezplacni vhod")
        elif 6 <= starost <= 17:
            print("cena: 5 EUR")
        elif 18 <= starost <= 64:
            print("cena: 8 EUR")
        else:
            print("cena: 6 EUR")
    else:
        print("nepravilen vnos dneva")

def vaja5():
    dni = int(input("vnesi stevilo dni:"))
    prihranki = 0
    dan1000 = 0
    for i in range(dni+1):
        if i % 7 != 0:
            prihranki += i
        if prihranki < 1000:
            dan1000 += 1
    print(f"Število dni: {dni}\nPrihranjeno: {prihranki} EUR\nVeč kot 1000 EUR na dan: {dan1000}")

import random as r

def vaja6():
    stevilo = r.randint(1,100)
    poskusi = 1
    while True:
        ugib = int(input(f"poskus {poskusi}: "))
        if ugib == stevilo:
            print(f"Bravo uganil si v {poskusi} poskusih")
            break
        elif ugib < stevilo:
            print("Vecje")
            poskusi += 1
        elif ugib > stevilo:
            print("manjse")
            poskusi += 1

def cena_s_popustom(cena,popust):
    pass

def main():
    # vaja1()
    # vaja2()
    # vaja3()
    # vaja4()
    # vaja5()
    # vaja6()
    cena = int(input("vnesi ceno: "))
    popust = int(input("vnesi % popusta: "))
    cena_s_popustom(cena, popust)

if __name__ == "__main__":
    main()