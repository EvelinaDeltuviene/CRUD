presents = [
            {
                "id":1,
                "name":"Saldainiai",
                "price":4.0,
                "receiver":"Janina"
            },
            {
                "id":2,
                "name":"Žvakė",
                "price":5.0,
                "receiver":"Marytė"
            },
            {
                "id":3,
                "name":"Kojinės",
                "price":6.0,
                "receiver":"Antanas"
            },
            {
                "id": 4,
                "name": "Namų kvapas",
                "price": 7.0,
                "receiver": "Viktoras"
            }
]
id_counter = 4
while True:
    print("--------------KALĖDOS--------------------")
    print("1. Pasirinkti dovaną")
    print("2. Pridėti naują dovaną")
    print("3. Redaguoti dovaną")
    print("4. Ištrinti dovaną")
    print("5. Išeiti ir uždaryti")
    print("------------PASIRINKITE: ------------------")
    option = input()
    match option:
        case "1":
            print("Dovanų sąrašas:")
            for pres in presents:
                print(f"{pres['id']}. Dovana: {pres['name']}. Kaina {pres['price']} Eur. Gavėjas: {pres['receiver']}")
        case "2":
            print("Įveskite dovaną:")
            name = input()
            print("Įveskite kainą:")
            price = float(input())
            print("Įveskite gavėją:")
            receiver = input()
            id_counter +=1
            pres = {"id": id_counter, "name": name, "price": price, "receiver": receiver}
            presents.append(pres)
        case "3":
            for pres in presents:
                print(f"{pres['id']}. Dovana: {pres['name']}. Kaina {pres['price']} Eur. Gavėjas: {pres['receiver']}")
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
        case "4":
            for pres in presents:
                print(f"{pres['id']}. Dovana: {pres['name']}. Kaina {pres['price']} Eur. Gavėjas: {pres['receiver']}")
            print("Įveskite ID dovanos, kurią norite trinti:")
            del_id = input()
            for pres in presents:
                if del_id == str(pres['id']):
                    print(pres)
                    pos = presents.index(pres)
                    del presents[pos]
                    break
        case "5":
            break






