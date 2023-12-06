#menu et programme principale qui gére la bibliothéque et fait appel aux classes: Adherent, Livre et Emprunt
from Adherent import Adherent
from Livre import Livre
from Emprunt import Emprunt
menu ="""
*************************************************
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
while True:
    print(menu)
    print("""
===================================================
================ Menu principal ===================
===================================================
    """)
    choix = input("Saisir votre choix selon le menu : ")
    if choix == "1":
        print("""
===================================================
================ Ajout d'adhérent =================
===================================================
        """)
        ad1 = Adherent()
        ad1.lireDepuisClavier()
        ad1.enregistrerDansFichier()
    elif choix == "2":
        print("""
===================================================
============ Suppression d'adhérent ===============
===================================================
        """)
        ad1 = Adherent()
        ad1.supprimerAdherent()
    elif choix == "3":
        print("""
===================================================
============== La liste des adhérents =============
===================================================
        """)
        ad1 = Adherent()
        ad1.afficherListeAdherent()
    elif choix == "4":
        print("""
===================================================
=============== Ajout de livre ====================
===================================================
        """)
        liv1 = Livre()
        liv1.lireDepuisClavier()
        liv1.enregistrerDansFichier()
    elif choix == "5":
        print("""
===================================================
============ Suppression de livre =================
===================================================
        """)
        liv1 = Livre()
        liv1.supprimerLivre()
    elif choix == "6":
        print("""
===================================================
================ La liste des livres ==============
===================================================
        """)
        liv1 = Livre()
        liv1.afficherListeLivre()
    elif choix == "7":
        print("""
===================================================
=============== Ajout d'emprunt ===================
===================================================
        """)
        em1 = Emprunt()
        em1.lireDepuisClavier()
        em1.enregistrerDansFichier()
    elif choix == "8":
        print("""
===================================================
================ Retour d'un livre ================
===================================================
        """)
        em1 = Emprunt()
        em1.supprimerEmprunt()
    elif choix == "9":
        print("""p
===================================================
============== La liste des emprunts  =============
===================================================
        """)
        em1 = Emprunt()
        em1.afficherListeEmprunt()
    elif choix == "Q" or choix == "q":
        print("""
===================================================
======== Vous avez quitté l'application ! =========
============ Merci d'avoire utiliser ==============
============== notre bibliothèque =================
===================================================
        """)
        break
    else:
        print("!!! Choix erroné! Saisir à nouveaux !!!  ")
