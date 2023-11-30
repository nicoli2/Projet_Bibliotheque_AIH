#menu et programme
menu = """*************************************************
*      Bienvenue à votre bibliothèque           *
*              Faites un choix :                *
*************************************************
*    1       Ajouter adhérent                   *
*    2       Supprimer adhérent                 *
*    3       Afficher tous les adhérent         * 
*    4       Ajouter Document                   *
*    5       Supprimer Document                 *
*    6       Afficher tous les Documents        *
*    7       Ajouter Emprunts                   *
*    8       Retour d’un Emprunts               *
*    9       Afficher tous les Emprunts         *
*    Q      Quitter                             *
*************************************************
 """
print(menu)


while True :
    choix = input("Saisir votre choix selon le menu :")
    if choix == "1" :
        print("Appeler un methode respective pour ajouter adhérent")
    elif choix == "2":
        print("Supprimer adhérent")
        print("Appeler un methode respective")
    elif choix == "3":
        print("Afficher tous les adhérent")
        print("Appeler un methode respective")
    elif choix == "4":
        print("Ajouter Document")
        print("Appeler un methode respective")
    elif choix == "5":
        print("Supprimer Document")
        print("Appeler un methode respective")
    elif choix == "6":
        print("Afficher tous les Documents")
        print("Appeler un methode respective")
    elif choix == "7":
        print("Ajouter Emprunts")
        print("Appeler un methode respective")
    elif choix == "8":
        print("Retour d’un  Emprunts")
        print("Appeler un methode respective")
    elif choix == "9":
        print("Afficher tous les Emprunts")
        print("Appeler un methode respective")
    elif choix == "Q" or choix == "q":
        print("Quitter, Merci d'avoire utiliser la bibliothèque ")
        break
    else :
        print("!!! Choix erroné! Saisie a nouveaux !!!  ")
