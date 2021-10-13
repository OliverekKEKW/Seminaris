import tkinter
import random
canvas = tkinter.Canvas(width=600, height=400)
canvas.pack()

#farba = f"#{random.randrange(256):02}"
x = 0
y = 0

for i in range(5):
    canvas.create_rectangle(x,y,x+50,y+50)


canvas.mainloop()
