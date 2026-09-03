def hello():
    oddelek = input("Kateri oddelek si? ")
    if oddelek.lower() == "1.ri":
        print(f"hello {oddelek} ♥")
    else:
        print(f"hello {oddelek}")

def postevanka():
    x = int(input("izberi si stevilo: "))
    st = 1
    while st <= 10:
        print(f"{x} * {st} = {x * st}")
        st += 1

if __name__ == "__main__":
    #hello()
    postevanka()