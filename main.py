from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createFile():
    try:
        readfileandfolder()
        name = input("Please tell your file name :- ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file : ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("File already exists")

    except Exception as err:
        print(f"An error occurred as {err}")

def readFile():
    try:
        readfileandfolder()
        name = input("Which file to read : ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)

            print("Done reading")
        else:
            print("The file doesn't exist")

    except Exception as err:
        print(f"An error occurred as {err}")

def updateFile():
    try:
        readfileandfolder()
        name = input("Select the file you want to update : ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("Press 1 for changing the file name")
            print("Press 2 to overwrite the file")
            print("Press 3 to append content in file")

            res = int(input("Tell your response : "))

            if res == 1:
                name2 = input("Enter the new file name : ")
                p2 = Path(name2)
                p.rename(p2)
                print(f"Name changed to {p2}")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Write the content : ")
                    fs.write(data)
                print("Content overwrite done")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Write the content you want to append : ")
                    fs.write(" " + data)
                print("Content appended successfully")

        else:
            print("File does not exist")

    except Exception as err:
        print(f"An error occurred as {err}")

def deleteFile():
    try:
        readfileandfolder()
        name = input("Enter the file name you want to delete : ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted successfully")
        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occurred as {err}")


while True:

    print("\n----- FILE MANAGER -----")
    print("Press 1 for creating the file")
    print("Press 2 for reading the file")
    print("Press 3 for updating the file")
    print("Press 4 for deleting the file")
    print("Press 5 to exit")

    check = int(input("Enter your response :- "))

    if check == 1:
        createFile()

    elif check == 2:
        readFile()

    elif check == 3:
        updateFile()

    elif check == 4:
        deleteFile()

    elif check == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid option")