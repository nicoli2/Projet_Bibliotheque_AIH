class Livre:
    def __init__(self, p_titre="", p_nbrPages="", p_ISBN=""):
        self.titre = p_titre
        self.nbrPages = p_nbrPages
        self.ISBN = p_ISBN
    def lireDepuisClavier(self):
        flag=1
        while flag == 1:
            n = input("Nbr de livres à ajouter : ")
            if n.isnumeric():
                x = 0
                while x < int(n):
                    print("========================")
                    self.titre = input("Titre: ")
                    self.nbrPages = input("Nbr de pages: ")
                    self.ISBN = input("ISBN: ")
                    d = str(self.titre) + ", " + str(self.nbrPages) + ", " + str(self.ISBN)
                    listeLivre.append(d)
                    x = x + 1
                print("========== Liste des livres ajoutés: ============")
                x = 0
                while x < int(n):
                    print("Livre num: ", x + 1, "\n", listeLivre[x])
                    x = x + 1
                print("====================================================")
                flag=0
            else:
                print("Saisie non accptée !!! Saisir un nombre ")
                flag=1
    def enregistrerDansFichier(self):
        f = open("livre.txt", "a")
        for x in listeLivre:
            f.write(x + "\n")
        f.close()
    def afficherListeLivre(self):
        f = open("livre.txt", "r")  # r: read, w: write, a: append
        ligne = f.readlines()
        print("ID, Titre, Nb de pages, ISBN")
        x = len(ligne)
        for i in range(0, x):
            print(i + 1, "-", ligne[i], end="")
        f.close()

    def supprimerLivre(self):
        f = open("livre.txt", "r")  # r: read, w: write, a: append
        ligne = f.readlines()
        flag = 1
        while flag == 1:
            x = input("Saisir l'ID de livre à supprimer: ")
            if x.isnumeric() and int(x) - 1 < len(ligne):
                flag = 0
                print("====== ATTENTION !!! Ce livre sera supprimé !!! =========")
                print("\n", ligne[int(x) - 1])
                print("===================================================================")
                y = input("Êtes-vous sûr de le supprimer ? O/N ")
                if y == "o" or y == "O":
                    listeTemp = []
                    for i in range(0, len(ligne)):
                        listeTemp.append(ligne[i])
                    listeTemp.pop(int(x) - 1)
                    f = open("livre.txt", "w")
                    for x in listeTemp:
                        f.write(x)
                    f.close()
                    print("========= Suppression de livre réussi =========")
                else:
                    print("============== Suppression de livre annulée =================")
                flag = 0
            else:
                print("Ce numéro de livre n'existe pas !!!")
                flag = 1

listeLivre = []
#Création d'objets
# liv1 = Livre()
# liv1.lireDepuisClavier()
# liv1.enregistrerDansFichier()
# print("=====La liste des livres=============")
# liv1.afficherListeLivre()
# liv1.supprimerLivre()


