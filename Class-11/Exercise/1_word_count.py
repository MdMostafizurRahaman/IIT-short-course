try:
    with open("poem.txt", "r") as file:
        content = file.read()
        words = content.split()
        print("Total words:", len(words))
except FileNotFoundError:
    print("poem.txt file not found.")