import json

def search():

    try: 
        with open("dictionary.json") as data:
            term_data = json.load(data)
        term = input("Enter Term: ").lower()
        print(f"{term.capitalize()}: {term_data[term]}")

    except KeyError:
        print("Term not found!")

def write():

    term = input("Enter Term: ")
    term_def = input("Enter Definition: ")

    with open("dictionary.json") as data:
        term_data = json.load(data)
    term_data[term] = term_def

    with open("dictionary.json", "w") as data:
        json.dump(term_data, data)

while True:
    inquiry = input("Enter [1] For Search [2] For Add Term [3] List All Words [4] For Exit\n-> ")

    if inquiry == "1":
        search()

    elif inquiry == "2":
        write()

    elif inquiry == "3":
        with open("dictionary.json") as data:
            term_data = json.load(data)
        for term, definition in term_data.items():
            print(f"{term.capitalize()}-> {definition.capitalize()}")
        save = input("Save in file? [y/n] ")

        if save == "y":
            file_type = input("Enter file type (csv,txt)\n-> ")

            if file_type == "csv":
                with open("words.csv", "w") as data:
                    for term, definition in term_data.items():
                        data.write(f"{term.capitalize()},{definition.capitalize()}\n")
                    print("Saved in words.csv !\n")

            elif file_type == "txt":
                with open("words.txt", "w") as file:
                    for term, definition in term_data.items():
                        file.write(f"{term.capitalize()}: {definition.capitalize()}\n")
                    print("Saved in words.txt !\n")

            else:
                print("File type not supported!\n")

    elif inquiry == "4":
        print("Have a Nice Day!")
        break

    else:
        print("Please enter a valid value!")
