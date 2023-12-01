#menu et programme
menu ="""*************************************************
*      Bienvenue à votre bibliothèque           *
*              Faites un choix :                *
*************************************************
*    1       Ajouter un adhérent                *
*    2       Supprimer un adhérent              *
*    3       Afficher tous les adhérents        * 
*    4       Ajouter un livre                   *
*    5       Supprimer un livre                 *
*    6       Afficher tous les livre            *
*    7       Ajouter un Emprunt                 *
*    8       Retour d’un Emprunt                *
*    9       Afficher tous les Emprunts         *
*    Q       Quitter                            *
*************************************************
 """
print(menu)
flag = 1
while flag == 1:
    choix = input("Saisir votre choix selon le menu : ")
    if choix == "1":
        print("============ Ajout d'adhérent =============")
        from Adherent import Adherent
        ad1 = Adherent()
        ad1.lireDepuisClavier()
        ad1.enregistrerDansFichier()
        flag = 1
    elif choix == "2":
        print("============ Suppression d'adhérent =============")
        from Adherent import Adherent
        ad1 = Adherent()
        ad1.supprimerAdherent()
        flag = 1
    elif choix == "3":
        print("============= La liste des adhérents ============")
        from Adherent import Adherent
        ad1 = Adherent()
        ad1.afficherListeAdherent()
        print("=================================================")
        flag = 1
    elif choix == "4":
        print("================ Ajout de livre =================")
        from Livre import Livre
        liv1 = Livre()
        liv1.lireDepuisClavier()
        liv1.enregistrerDansFichier()
        flag = 1
    elif choix == "5":
        print("============= Suppression de livre ==============")
        from Livre import Livre
        liv1 = Livre()
        liv1.supprimerLivre()
        flag = 1
    elif choix == "6":
        print("=============== La liste des livres =============")
        from Livre import Livre
        liv1 = Livre()
        liv1.afficherListeLivre()
        print("=================================================")
        flag = 1
    elif choix == "7":
        print("Ajouter Emprunts")
        print("Appeler un methode respective")
        flag = 1
    elif choix == "8":
        print("Retour d’un  Emprunts")
        print("Appeler un methode respective")
        flag = 1
    elif choix == "9":
        print("Afficher tous les Emprunts")
        print("Appeler un methode respective")
        flag = 1
    elif choix == "Q" or choix == "q":
        print("Quitter, Merci d'avoire utiliser la bibliothèque ")
        break
    else:
        print("!!! Choix erroné! Saisir à nouveaux !!!  ")
        flag = 1
