def sekaj(text, cislo):
    i = 0
    while i <= len(text):
        i += cislo
        text = text[:i] + "\n" + text[i:]
        i += 1
    return (text)


x = int(input("cislo:"))
hym = "Ja sladké túžby, túžby po kráse spievam peknotou nadšený, a v tomto duše mojej ohlase svet môj je celý zavrený; z výsosti Tatier ona mi svieti, ona mi z ohňov nebeských letí, ona mi svety pohýna; ona mi kýva zo sto životov: No centrom, živlom, nebom, jednotou krás mojich moja Marína!"

print(sekaj(hym, x))
