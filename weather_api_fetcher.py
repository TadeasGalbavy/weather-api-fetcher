import requests
from pprint import pprint

def nacitaj_mesta():

    zoznam_miest = []

    while True:
        nazov_mesta = input("Zadaj názov mesta: ").strip()

        if nazov_mesta in zoznam_miest:
            print("Toto mesto si už zadal, zadaj iné.")
        else:
            zoznam_miest.append(nazov_mesta)

        pokracovanie = input("Chceš pokračovať? (ano/nie)").strip().lower()

        if pokracovanie == "nie":
            break

    return zoznam_miest

def ziskaj_pocasie_pre_mesto(mesto):

    api_key = "f78cc36682d19d151667e0c3da66305f"

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={mesto}&appid={api_key}&units=metric")

    if response.status_code == 200:
        data = response.json()

        teplota = data["main"]["temp"] 
        vlhkost = data["main"]["humidity"]
        pocitova = data["main"]["feels_like"]
        obloha = data["weather"][0]["description"]
        vietor = data["wind"]["speed"]

        return {
            "teplota": teplota,
            "vlhkost": vlhkost,
            "pocitova": pocitova,
            "obloha": obloha,
            "vietor": vietor
        }

    else:
        print(f"Mesto {mesto} sa nepodarilo násjť.")
        return None

def vypis_pocasie(mesto, data):
    print(f"Počasie pre mesto: {mesto.capitalize()}\n- teplota: {data["teplota"]}\n- vlhkosť: {data["vlhkost"]}\n- pocitová teplota: {data["pocitova"]}\n- obloha: {data["obloha"]}\n- rýchlosť vetra: {data["vietor"]}.\n")

def main():
    zoznam_miest = nacitaj_mesta()
    for mesto in zoznam_miest:
        ziskanie_dat = ziskaj_pocasie_pre_mesto(mesto)
        if ziskanie_dat:
            vypis_pocasie(mesto, ziskanie_dat)

if __name__ == "__main__":
    main()