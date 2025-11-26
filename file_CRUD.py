from data import load_presents
import csv

headers = ["id", "name", "price", "receiver"]

def load_presents():
    with open("presents.csv", mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def save_presents(presents):
    with open("presents.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(presents)

def create_presents(id_counter, presents):          #2.
    print("Įveskite dovaną:")
    name = input()
    print("Įveskite kainą:")
    price = float(input())
    print("Įveskite gavėją:")
    receiver = input()
    id_counter += 1
    pres = {"id": id_counter, "name": name, "price": price, "receiver": receiver}
    presents.append(pres)
    save_presents(presents)
    return id_counter

def edit_presents(presents):            #3.
    print_presents(presents)
    print("Įveskite ID dovanos, kurią norite redaguoti:")
    edit_id = input()
    for pres in presents:
        if edit_id == str(pres['id']):
            print("Įveskite dovanos pavadinimą:")
            pres['name'] = input()
            print("Įveskite kainą:")
            pres['price'] = float(input())
            print("Įveskite gavėją:")
            pres['receiver'] = input()
            break
    save_presents(presents)

def delete_presents(presents):          #4.
    print_presents(presents)
    print("Įveskite ID dovanos, kurią norite trinti:")
    del_id = input()
    for pres in presents:
        if del_id == str(pres['id']):
            pos = presents.index(pres)
            del presents[pos]
            break
    save_presents(presents)

def print_info():
    print("--------------KALĖDOS--------------------")
    print("1. Pasirinkti dovaną")
    print("2. Pridėti naują dovaną")
    print("3. Redaguoti dovaną")
    print("4. Ištrinti dovaną")
    print("5. Išeiti ir uždaryti")
    print("------------PASIRINKITE: ------------------")

def print_presents(presents):
    for pres in presents:
        print(f"{pres['id']}. Dovana: {pres['name']}. Kaina {pres['price']} Eur. Gavėjas: {pres['receiver']}")