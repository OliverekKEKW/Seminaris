samohlasky = "aeiouóíúéý"
riekanka = "sedí mucha na stene a spí "
print(riekanka)
def zamena(text,n):
    for znak in samohlasky:
        text = text.replace(znak,n)
    print(text)


n = input("Vložiš samohlásku:")
zamena(riekanka,n)
