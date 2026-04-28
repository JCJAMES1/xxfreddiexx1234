try:
    with open ("freddie.txt", "x") as file:
        print("File created successfully.")
        file.write("Freddie laban sa lahat")
except FileExistsError:
    print("File already exists.")