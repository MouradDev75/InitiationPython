# Fonction: est un bloc d'instructions réutilisable

# 2 types de fonctions:
# fonction qui renvoie un résultat: input()
# fonction qui ne renvoie aucun résultat: print()

# Syntaxe pour créer une fonction: def nom_fonction(paramètres): instructions

# Exemple d'une fonction sans paramètres:

def my_fonction():
    print('texte...........')

# Appelle de my_function:

my_fonction()

# Sans les 2 parenthèses, il s'agit d'une variable contenant l'id de la fonction en mémoire
my_fonction

# Exemple d'une fonction avec des paramètres

def repeter(texte, nombre_de_fois):
    # for i in range(nombre_de_fois):
    #     print(texte)

    compteur = 0
    while True:
        print(texte)
        compteur += 1
        if compteur == nombre_de_fois:
            break

repeter('hello', 4)

# exemple d'une fonction qui renvoie un résultat

def somme(x, y):
    return x + y

r = somme(10,15)

print(f"somme = {r}")