import requests as r

def vaja1(a, b):
    l = ["USD","GBP","CHF","JPY"] # list of currency types
    i = 0
    if b.status_code == 200: # check to see if everything is aight
        print(f"Tečaji na dan {a["date"]}") # if all good
        while i < len(l):
            print(a["rates"][l[i]])
            i += 1
        print(f"Skupaj valut {i}")
    else:
        print("Prišlo je do napake") # if all bad

def v_tujo(a):
    znesek = float(input("Vnesi znesek v EUR: "))
    valuta = input("Vnesi v katero valuto bi pretvoril: ")
    valuta = valuta.upper()
    if valuta not in a["rates"]:
        print(f"Valuta {valuta} ne obstaja")
    else:
        print(f"{a["amount"]*znesek} EUR = {round(a["rates"][valuta]*znesek, 2)} {valuta}")

def v_evre(a):
    valuta = input("Vnesi valuto: ")
    znesek = float(input("Vnesi znesek: "))
    valuta = valuta.upper()
    mult = round(znesek/a["rates"][valuta], 2)
    if valuta not in a["rates"]:
        print(f"Valuta {valuta} ne obstaja")
    else:
        print(f"{round(a["rates"][valuta]*mult, 0)} {valuta} = {a["amount"]*mult} EUR")

def vaja3(a):
    datum = a["rates"]
    nuhuh = None
    for date, values in datum.items():
        rate = values["USD"]
        if nuhuh is None:
            print(f"{date}: {rate}")
        elif rate > nuhuh:
            print(f"{date}: {rate} (gor)")
        elif rate < nuhuh:
            print(f"{date}: {rate} (dol)")
        else:
            print(f"{date}: {rate} (nespremenjen)")
        nuhuh = rate

def vaja4(a):
    koli = a["rates"]
    valute = ["USD", "GBP", "CHF"]
    for val1 in valute:
        for val2 in valute:
            if val1 == val2:
                continue
            tec = koli[val2] / koli[val1]
            print("1", val1, "=", round(tec, 4), val2)

def vaja5(a):
    datum = a["rates"]
    valu = None
    rezUP = []
    rezDAT = []
    rezDOWN = []
    rezTAD = []
    for date, values in datum.items():
        rate = values["GBP"]
        if rate*800 > 800:
            rezUP.append(rate)
            rezDAT.append(date)
        else:
            rezDOWN.append(rate)
            rezTAD(date)



def main():
    fran = r.get("https://api.frankfurter.dev/v1/latest")
    fran2 = r.get("https://api.frankfurter.dev/v1/2026-09-01..2026-09-07?symbols=USD")
    fran3 = r.get("https://api.frankfurter.dev/v1/2026-09-01..2026-09-30?symbols=GBP")
    franJSON = fran.json()
    franSON = fran2.json()
    franON =fran3.json()
    # vaja1(franJSON, fran)
    # v_tujo(franJSON)
    # v_evre(franJSON)
    # vaja3(franSON)
    # vaja4(franJSON)
    vaja5(franON)

if __name__ == "__main__":
    main()