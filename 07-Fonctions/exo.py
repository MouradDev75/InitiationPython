#1)
def somme_liste(entiers):

    s = 0
    for e in entiers:
        s = s + e

    return s

print(somme_liste([2,7,3,5]))

#2)

def moyenne_liste(entiers):
    s = somme_liste(entiers)

    nb = 0
    for e in entiers:
         nb = nb + 1

    return s / nb

print(moyenne_liste([1,2]))