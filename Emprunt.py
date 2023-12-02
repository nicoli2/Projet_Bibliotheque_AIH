class Emprunt:
    def __init__(self, p_titre="", p_nom="", p_date=""):
        self.titre = p_titre
        self.nom = p_nom
        self.date = p_date
    def lireDepuisClavier(self):
        flag=1
        while flag == 1:
            n = input("Nbr d'emprunts à ajouter : ")
            if n.isnumeric():
                x = 0
                while x < int(n):
                    print("===============================================")
                    self.titre = input("Titre de livre: ")
                    self.nom = input("Nom de l'emprunteur: ")
                    self.date = input("Date de l'emprunt: ")
                    d = str(self.titre) + ", " + str(self.nom) + ", " + str(self.date)
                    listeEmprunt.append(d)
                    x = x + 1
                print("========== Liste des emprunts ajoutés: ============")
                x = 0
                while x < int(n):
                    print("Emprunt num: ", x + 1, "\n", listeEmprunt[x])
                    x = x + 1
                print("====================================================")
                flag=0
            else:
                print("Saisie non accptée !!! Saisir un nombre ")
                flag=1
    def enregistrerDansFichier(self):
        f = open("emprunt.txt", "a")
        for x in listeEmprunt:
            f.write(x + "\n")
        f.close()
    def afficherListeEmprunt(self):
        f = open("emprunt.txt", "r")  # r: read, w: write, a: append
        ligne = f.readlines()
        print("ID, Titre, Nom emprunteur, Date")
        x = len(ligne)
        for i in range(0, x):
            print(i+1,"-", ligne[i], end="")
        f.close()
    def supprimerEmprunt(self):
        f = open("emprunt.txt", "r")  # r: read, w: write, a: append
        ligne = f.readlines()
        flag = 1
        while flag == 1:
            x = input("Saisir l'ID d'e l'emprunt à supprimer: ")
            if x.isnumeric() and int(x)-1 < len(ligne):
                flag = 0
                print("====== ATTENTION !!! Cet emprunt sera supprimé !!! =========")
                print("\n", ligne[int(x)-1])
                print("===================================================================")
                y = input ("Êtes-vous sûr de vouloir le supprimer ? O/N ")
                if y == "o" or y == "O":
                    listeTemp = []
                    for i in range(0, len(ligne)):
                        listeTemp.append(ligne[i])
                    listeTemp.pop(int(x)-1)
                    f = open("emprunt.txt", "w")
                    for x in listeTemp:
                        f.write(x)
                    f.close()
                    print("========= Suppression d'emprunt réussi =========")
                else:
                    print("============== Suppression d'emprunt annulée =================")
                flag = 0
            else:
                print("Ce numéro d'emprunt n'existe pas !!!")
                flag = 1
listeEmprunt = []
#Création d'objets
# em1 = Emprunt()
# em1.lireDepuisClavier()
# em1.enregistrerDansFichier()
# print("=====La liste des emprunts=============")
# em1.afficherListeEmprunt()
# # em1.supprimerEmprunt()



