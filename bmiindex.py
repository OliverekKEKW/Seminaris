import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

vaha = float(input("Váha v kilogramoch:"))
výška = float(input("Výška v metroch:"))


def vypocetbmi(vyska, hmotnost):
        vyska = výška
        hmotnost = vaha
        vyska = vyska / 100
        bmi = hmotnost / (hmotnost ** 2)
        bmi =
        return bmi, vyska, hmotnost

if 0 < bmi < 17,5:
    vysledok = "Tvoje BMI je " + str(bmi) + "Výsledok: podvýživa"
elif 17.5 < bmi < 25.0:
    vysledok = "Tvoje BMI je " + str(bmi) + "Výsledok: ideálna a zdravá váha"
elif 25 < bmi < 30:
    vysledok = "Tvoje BMI je " + str(bmi) + "Výsledok: mierna nadvaha"
elif 30 < bmi < 40:
    vysledok = "Tvoje BMI je " + str(bmi) + "Výsledok: obezita"
else bmi > 40:
    vysledok = "Tvoje BMI je " + str(bmi) + "Výsledok: ťažká obezita"

def ciara():
    canvas.create_rectangle(0,100,120,200)
    canvas.create_rectangle(120,100,150,200)
    canvas.create_rectangle(150,100,180,200)
    canvas.create_rectangle(180,100,300,200)
    #canvas.create_line(a, 70, a, 230)


canvas.mainloop()


