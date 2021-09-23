abeceda = 'aáäbcčdďeéfghiíjklĺľmnňoóôpqrŕsštťuúvwxyýzž'
text = "Stojí, stojí mohyla. Na mohyle zlá chvíľa, na mohyle tŕnie, chrastie a v tom tŕní,"
for pismeno in abeceda:
    pocet = 0
    for znak in text:
        if pismeno == znak.lower():
            pocet +=1
    print(f"{pismeno}: {pocet}")

