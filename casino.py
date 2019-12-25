import time
import random

sous = 0
essai = 0
while sous <= 0:
    ok = False
    while not ok:
        sous = input("Avec combien de sous voulez-vous commencer ? => ")
        try:
            sous = int(sous)
            ok = True
        except ValueError:
            print("Il faut renseigner un nombre")
            ok = False
    if sous <= 0:
        essai += 1
        if essai > 10:
            print("Bon, c'est bon t'as fini ? Tu voudrais pas faire quelque chose de plus intéressant ?")
        elif essai > 15:
            print("Ca devient vraiment lourd là !")
        else:
            print("Il faut que ce soit positif")
    else:
        print("Ok, vous commencez avec : {}€".format(str(sous)))

while sous > 0:
    ok = False
    while not ok:
        print("Argent : {}€".format(str(sous)))
        miseStr = True
        while miseStr:
            mise = input("Combien voulez-vous miser ? =>")
            try:
                mise = int(mise)
                miseStr = False
            except ValueError:
                print("Il faut renseigner un nombre")
        if mise < sous:
            print("Vous ne pouvez pas miser plus que ce que vous avez !")
        else:
            print("Très bien ! Votre mise est de {}€".format(str(mise)))
            ok = True
    sous = sous - mise
    print("Bien il vous reste donc {}€".format(str(sous)))

    ok = False
    while not ok:
        numUserStr = True
        while numUserStr:
            numeroUtilisateur = input("Sur quel numéro entre 1 et 6 voulez-vous miser ?")
            try:
                numeroUtilisateur = int(numeroUtilisateur)
                numUserStr = False
            except ValueError:
                print("Il faut renseigner un nombre")
        if numeroUtilisateur < 1 or numeroUtilisateur > 6:
            prin("Il faut rentrer un numéro entre 1 et 6 !")
        else:
            print("Très bien ! vous misez donc sur le ", numeroUtilisateur)
            ok = True
    
    print("Pour récapituler, vous misez {}€ sur le {}".format(mise, numeroUtilisateur))
    print("Maintenant je lance le dé :")
    time.sleep(random.randrange(0, 3))
    lancerDe = random.randint(1, 6)
    