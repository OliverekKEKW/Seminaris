import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()
zoznam = []
pat = 0
styri = 0
for i in range(1000):
    ciselko = random.randrange(100, 1000)
    zoznam.append(ciselko)
    if ciselko % 5 == 0:
        pat +=1
    elif ciselko % 4 ==0:
        styri +=1

print(zoznam)
print(pat)
print(styri)



def stlpec(hodnota, max, poradie):
    vyska = hodnota / max * 200
    canvas.create_rectangle(poradie * 20, 200, 20 + poradie * 20, 200 -
                            vyska, fill="blue")
    canvas.create_text(10 + poradie * 20, 220,text=str(hodnota))

max = 0
pole = []


canvas.mainloop()

