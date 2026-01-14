with open("words.txt", "r", encoding="utf-8") as file:
    content = file.read()
    content = content.split("\n")
    for i in range(10, len(content)):
       print(content[i],end="\n")
