import tkinter
canvas = tkinter.Canvas()
#kreslenie jedného stĺpca
def stlpec(hodnota, max, poradie):
    vyska = hodnota / max * 200
    canvas.create_rectangle(poradie * 20, 200, 20 + poradie * 20, 200 -
                            vyska, fill="blue")
    canvas.create_text(10 + poradie * 20, 220,text=str(hodnota))
max = 0
pole = []
# nacitanie vysok stlpcov
while True:
    vyska = int(input("Zadaj výšku stĺpca: "))
    if vyska < 0:
        break
    pole.append(vyska)
    if vyska > max:
        max = vyska
#vykreslenie stĺpcov
canvas.pack()
i = 1
for vyska in pole:
    stlpec(vyska, max, i)
    i += 1
canvas.mainloop()
