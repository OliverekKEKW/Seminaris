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

def bublinkovy(nz):
    z = list(nz)
    n=len(z)
    for i in range(n):
        for j in range(n-1):
            if z [j] > z[j + 1]:
                z[j], z[j+1] = z[j+1], z[j]
    return z

def bublinkovy2(nz):
    z = list(nz)
    krok=0
    n=len(z)
    for j in range(n):
        for i in range(j,n):
            if z[i] < z[j]:
                z[i], z[j] = z[j], z[i]
    return z
n = 25
zoz = nahodnecisla(n, 100, 150)
print(zoz)
print(bublinkovy(zoz))
print(bublinkovy2(zoz))





