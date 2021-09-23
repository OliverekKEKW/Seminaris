import random

def generuj_heslo (pm,pv,pc,pz):
    male = "abcdefghijklmnopqrstuvwxyz"
    velke = male.upper()
    cislo = "0123456789"
    znakheslo = ""
    for i in range(pm):
        znakheslo += random.choice(male)
    for i in range(pv):
        znakheslo += random.choice(velke)
    for i in range(pc):
        znakheslo += random.choice(cislo)
    for i in range(pz):
        znakheslo += random.choice("+-*/?.:@&#")
    heslo = ""
    while len(znakheslo) > 0:
        i = random.randrange(len(znakheslo))
        heslo += znakheslo[i]
        znakheslo = znakheslo[:i] + znakheslo[i+1:]
    return heslo


m = int(input("pocet malych:"))
v = int(input("pocet velkych:"))
c = int(input("pocet cisel:"))
z = int(input("pocet znakov:"))


print(generuj_heslo(m,v,c,z))

