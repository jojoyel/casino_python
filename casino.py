import time
import random
import os

sous = 0
essai = 0
nomFichier = "sauvegarde.txt"
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
    if sous == -123:
        print("Récupération du fichier de sauvegarde")
        fichier = open(nomFichier, "r")
        sous = int(fichier.read())
        fichier.close()
        print("Ok, vous reprennez avec : {}€".format(str(sous)))
    elif sous <= 0:
        essai += 1
        if essai > 10:
            print("Bon, c'est bon t'as fini ? Tu voudrais pas faire quelque chose de plus intéressant ?")
        elif essai > 15:
            print("Ca devient vraiment lourd là !")
        else:
            print("Il faut que ce soit positif")
    else:
        print("Ok, vous commencez avec : {}€".format(str(sous)))

continuer = True
while sous > 0 and continuer == True:
    ok = False
    while not ok:
        print("Argent : {}€".format(str(sous)))
        miseStr = True
        while miseStr:
            mise = input("Combien voulez-vous miser ? => ")
            try:
                mise = int(mise)
                miseStr = False
            except ValueError:
                print("Il faut renseigner un nombre")
        if mise > sous:
            print("Vous ne pouvez pas miser plus que ce que vous avez !")
        elif mise < 0:
            print("Peuh ! Vous ne pouvez pas miser moins que zéro")
        else:
            print("Très bien ! Votre mise est de {}€".format(str(mise)))
            ok = True
    sous = sous - mise
    print("Bien il vous reste donc {}€".format(str(sous)))

    ok = False
    while not ok:
        numUserStr = True
        while numUserStr:
            numeroUtilisateur = input("Sur quel numéro entre 1 et 6 voulez-vous miser ? => ")
            try:
                numeroUtilisateur = int(numeroUtilisateur)
                numUserStr = False
            except ValueError:
                print("Il faut renseigner un nombre")
        if numeroUtilisateur < 1 or numeroUtilisateur > 6:
            print("Il faut rentrer un numéro entre 1 et 6 !")
        else:
            print("Très bien ! vous misez donc sur le ", numeroUtilisateur)
            ok = True
    
    print("Pour récapituler, vous misez {}€ sur le {}".format(mise, numeroUtilisateur))
    print("Maintenant je lance le dé :")
    time.sleep(random.randrange(0, 3))
    lancerDe = random.randint(1, 6)
    print("Le dé est tombé sur : ")
    input("")
    print("le ", lancerDe)
    if lancerDe == numeroUtilisateur:
        print("Bravo vous êtes tombé sur le bon numéro !")
        print("Vous gagnez le double de votre mise !")
        sous = sous + mise * 2
        print("Vous ressortez donc avec {}€".format(str(sous)))
    elif lancerDe == numeroUtilisateur - 1 or lancerDe == numeroUtilisateur + 1:
        print("Vous y étiez presque !")
        print("Vous êtes dédomagé de la moitié de votre mise")
        sous = sous + mise // 2
    else:
        print("Oof ! Vous êtes totalement à coté ! Vous aevz parié sur le ", str(numeroUtilisateur))
        print("Vous ne récupérez rien")
    print("Vous avez {}€".format(str(sous)))
    reponse = input("Voulez-vous continuer (Oui/O) ? => ")
    if reponse == "O" or reponse == "o" or reponse == "Oui":
        print("Super ! On continue !")
    else:
        print("Voulez-vous enregistrer vos sous dans un fichier pour pouvoir le récupérer plus tard ?")
        enregistrer = input("Voulez-vous enregistrer ?")
        if enregistrer == "Oui" or enregistrer == "O" or enregistrer == "o":
            print("Bien, écriture dans un fichier")
            fichier = open(nomFichier, "w")
            fichier.write(str(sous))
            fichier.close()
        else:
            print("Ok à bientôt !")
        continuer = False