from list_CRUD import *
from data import load_presents

presents = load_presents()

id_counter = 4
while True:
    print_info()
    option = input()
    match option:
        case "1":
            print_presents(presents)
        case "2":
            id_counter = create_presents(id_counter, presents)
        case "3":
            edit_presents(presents)
        case "4":
            delete_presents(presents)
        case "5":
            break