#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' TAFSIR NDICKE LAYE DIOP
        09-06-2017'''

# on importe le table ascii lowercase qui contient les lettres minuscules de l'alphabet
from string import ascii_lowercase


# cette methode permet de retourner un tableau contenant les differents mots encodés d'une phrase
def codechains(ch, rotation):
    result = []
    # la methode split permet de remplir dans un tableau les differents mots dune phrase séparés par espace (1)
    chaine1 = chaine.split()
    for a in chaine1:
        mot = ""
        for b in a:
            # on verifie si le caractère se trouve dans ascii_lowercase, sinon, le caractère nest pas décodée et est ajouté
            # directement au mot
            if not (b in ascii_lowercase):
                mot += b
            # vu que les lettres dans ascii_lowercase sont indexes de 0 à 25 , si la somme de lindex de b et
            # de la rotation est superieur à 25 on fait la difference entre 25 et la rotation, on y ajoute 1
            # et on le retranche de l'index de b pour pouvoir commencer le comptage à partir de l'index de a
            # qui est 0 sommé à cette difference trouvée
            elif ascii_lowercase.index(b) + int(rotation) > 25:
                x = ascii_lowercase.index(b) - ((25 - rotation) + 1)
                mot += ascii_lowercase[0 + x]
            # sinon on ajoute juste à lindex de b la valeur de la rotation et on ajoute à mot la lettre
            # correspondant à cet nouvel index
            else:
                reserv = ascii_lowercase.index(b) + int(rotation)
                mot += ascii_lowercase[reserv]
        # on ajoute à chaque fois le mot encodé à un tableau qui sera retourné par la méthode
        result.append(mot)
    return result


# la methode permettant de retourner sous forme de tableau une chaine de caractères décodée
def decodechains(ch, rotation):
    result = []
    # (1)
    chaine1 = chaine.split()
    for a in chaine1:
        mot = ""
        for b in a:
            # on verifie si le caractère se trouve dans ascii_lowercase, sinon, le caractère nest pas décodée et est ajouté
            # directement au mot
            if not (b in ascii_lowercase):
                mot += b
            # si la rotation est supérieure à l'index de b, on fait la difference entre la rotation
            # et l'index puis et on retranche un à ce resultat. ensuite, on se positionne à la fin
            # de la table ascii_ lowercase et retranche 25(index de z) à la difference antérieurement trouvée
            elif int(rotation) > ascii_lowercase.index(b):
                x = (rotation - ascii_lowercase.index(b)) - 1
                mot += ascii_lowercase[25 - x]
            # sinon on retranche à lindex de b la valeur de la rotation
            else:
                reserv = ascii_lowercase.index(b) - int(rotation)
                mot += ascii_lowercase[reserv]
        result.append(mot)
    return result


def menu():
    print('           BIENVENUE             ')

    print('----------------------------------')
    print('|    1- ENCODAGE                 |')
    print('|    2- DECODAGE                 |')
    print('|    3- QUITTER                  |')
    print('----------------------------------')
    return


menu()
recup = int(input("selectionner l'operation à faire: "))
while recup != 3:
    if recup == 1:
        result = " "
        chaine = input("choisir la chaine: ")
        rotation = int(input("choisir la rotation(compris entre 1 et 25) : "))
        # on sassure que la valeur de la rotation doit etre compris entre 1 et 25
        while rotation < 1 or rotation > 25:
            rotation = int(input("rotation doit etre compris entre 1 et 25, reessayez: "))
        # on fait appel à la methode codechains quon recupere dans une variable
        variable = codechains(chaine, rotation)
        # on parcours la variable et on concatène les mots du tableau de sorte
        # à avoir une phrase(eviter de l'afficher sous forme de tableau)
        for i in variable:
            result += i + " "
        print ("la chaine encodée est: " + result)
        menu()
        recup = int(input("selectionner l'operation à faire: "))
    elif recup == 2:
        result = " "
        chaine = input("choisir la chaine: ")
        rotation = int(input("choisir la rotation: "))
        while rotation < 1 or rotation > 25:
            rotation = input("rotation non valide, ressayez: ")
        # on fait appel à la methode decodechains
        variable = decodechains(chaine, rotation)
        for i in variable:
            result += i + " "
        print ("La chaine décodée est: " + result)
        menu()
        recup = int(input("selectionner l'operation à faire: "))

    else:
        # on notifie que l'entrée est invalide si l'utilisateur saisait un caractere
        # autre que 1,2 ou 3
        print("Entrée invalide")
        menu()
        recup = int(input("selectionner l'operation à faire: "))
if recup == 3:
    # on quitte le projet si la valeur saisie est égale à 3
    print("au revoir!!")
    exit()