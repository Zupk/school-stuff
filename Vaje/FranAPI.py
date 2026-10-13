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
    i = 0
    print(a["rates"]["2026-09-01"])
    while i < 7:
        
        i += 1


def main():
    fran = r.get("https://api.frankfurter.dev/v1/latest")
    fran2 = r.get("https://api.frankfurter.dev/v1/2026-09-01..2026-09-07?symbols=USD")
    franSON = fran2.json()
    franJSON = fran.json()
    # vaja1(franJSON, fran)
    # v_tujo(franJSON)
    # v_evre(franJSON)
    vaja3(franSON)

if __name__ == "__main__":
    main()