def ref():
    dijak = {
        "ime": "Ana",
        "starost": 17,
        "razred": "3. RA"
    }

    print(dijak["ime"])      # Ana
    print(dijak["starost"])  # 17
def nal1():
    avto = {
            "znamka" : "Porsche",
            "model" : "GT 911",
            "letnik" : 2018
            }
    avto["barva"] = "white"
    print(avto["znamka"])
    print(avto["model"])
    print(avto["letnik"])
    print(avto["barva"])

def nal2():
    sola = {
    "ime": "ŠC Kranj",
    "naslov": {
        "ulica": "Kidričeva cesta 55",
        "posta": 4000,
        "kraj": "Kranj"
        },
        "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
    }

    print(sola["naslov"]["kraj"])   # Kranj
    print(sola["smeri"][0])         # računalništvo
    print(len(sola["smeri"]))       # 3
    print(sola["naslov"]["posta"])
    i = 0
    while i < len(sola["smeri"]):
        print(sola["smeri"][i])
        i += 1

def nal3():
    vreme = {
             "latitude": 46.06,
             "longitude": 14.5,
             "current_units": {
                "temperature_2m": "°C",
                "wind_speed_10m": "km/h"
                },
             "current": {
                 "time": "2026-10-06T10:00",
                 "temperature_2m": 14.2,
                 "wind_speed_10m": 6.8
                }
            }
    print(vreme["current"]["temperature_2m"])
    print(vreme["current"]["wind_speed_10m"], vreme["current_units"]["wind_speed_10m"])
    print(vreme["latitude"])


def nal4():
    pass

def main():
    nal3()


if __name__ == "__main__":
    main()