import random
def zoznam(a,b):
    zoznam = []
    for i in range(a):
        cisla = random.randrange(0,b)
        zoznam.append(cisla)
    return zoznam
c = zoznam(25,100)
print(c)

def nahodnecisla(poc=10, od=0, do=100):
    from random import randrange
    cisla1=[]
    for i in range(poc):
        cisla1.append(randrange(od, do+1))
    return cisla1

n = 25
zoz = nahodnecisla(n, 100, 150)
print(zoz)





