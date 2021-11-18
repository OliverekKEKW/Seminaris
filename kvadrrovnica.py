import tkinter
from math import sqrt
canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

a = float(input("Zadaj a:"))
b = float(input("Zadaj b:"))
c = float(input("Zadaj c:"))

d = (b**2) - (4*a*c)
if d < 0:
    print("Nemá riešenie")
elif d == 0:
    print(f"Rovnica má jedno riešenie: {(-b+sqrt(d))/(2*a)}")
else:
    print("Rovnica má 2 riešenia: {} a {}".format(
        (-b+sqrt(d))/(2*a),
        (-b-sqrt(d))/(2*a)

))
suradnice = []
canvas.create_line(0, 300, 600, 300)
canvas.create_line(300, 0, 300, 600)
#canvas.create_text(250,10,text = "Koreň prvý == "+str(vysledok1) + " Koreň druhý == "+ str(vysledok2),font="Arial 10")

for x in range(-300, 300):
    y = a*x*x + x*b + c
    suradnice.append(x + 300)
    suradnice.append(-y + 300)

print(suradnice)
canvas.create_line(suradnice, fill="red")
print("Diskriminant vyšiel:", d)












canvas.mainloop()
