import turtle
import random
tabula = turtle.Screen()
pero = turtle.Turtle()
#pero.speed(0)

def rgb():
    return '#{:02x}{:02x}{:02x}'.format(random.randrange(256),random.randrange(256),random.randrange(256))

def terc():
    r = 100
    for i in range(20):
        pero.dot(r, rgb())
        r -= 5


terc()
tabula.mainloop()
