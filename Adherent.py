class Adherent:
    def __init__(self, p_nom="", p_prenom="", p_num=""):
        self.nom = p_nom
        self.prenom = p_prenom
        self.num = p_num
    def lireDepuisClavier(self):
        flag=1
        while flag == 1:
            n = input("Nbr d'adhérents à ajouter : ")
            if n.isnumeric():
                x = 0
                while x < int(n):
                    print("===============================================")
                    self.nom = input("Nom d'adhérent: ")
                    self.prenom = input("Prénom d'adhérent: ")
                    self.num = input("Num d'adhérent: ")
                    d = str(self.nom) + ", " + str(self.prenom) + ", " + str(self.num)
                    listeAdherent.append(d)
                    x = x + 1
                print("========== Liste des adhérents ajoutés: ============")
                x = 0
                while x < int(n):
                    print("Adhérent num: ", x + 1, "\n", listeAdherent[x])
                    x = x + 1
                print("====================================================")
                flag=0
            else:
                print("Saisie non accptée !!! Saisir un nombre ")
                flag=1
    def enregistrerDansFichier(self):
        f = open("adherent.txt", "a")
        for x in listeAdherent:
            f.write(x + "\n")
        f.close()
    def afficherListeAdherent(self):
        f = open("adherent.txt", "r")  # r: read, w: write, a: append
        ligne = f.readlines()
        print("ID, Nom, Prénom, Numéro")
        x = len(ligne)
        for i in range(0, x):
            print(i+1,"-", ligne[i], end="")
        f.close()
    def supprimerAdherent(self):
        f = open("adherent.txt", "r")  # r: read, w: write, a: append
        ligne = f.readlines()
        flag = 1
        while flag == 1:
            x = input("Saisir l'ID d'adhérent à supprimer: ")
            if x.isnumeric() and int(x)-1 < len(ligne):
                flag = 0
                print("====== ATTENTION !!! Cet adhérent sera supprimé !!! =========")
                print("\n", ligne[int(x)-1])
                print("===================================================================")
                y = input ("Êtes-vous sûr de le supprimer ? O/N ")
                if y == "o" or y == "O":
                    listeTemp = []
                    for i in range(0, len(ligne)):
                        listeTemp.append(ligne[i])
                    listeTemp.pop(int(x)-1)
                    f = open("adherent.txt", "w")
                    for x in listeTemp:
                        f.write(x)
                    f.close()
                    print("========= Suppression d'adhérent réussi =========")
                else:
                    print("============== Suppression d'adhérent annulée =================")
                flag = 0
            else:
                print("Ce numéro d'adhérent n'existe pas !!!")
                flag = 1
listeAdherent = []
#Création d'objets
# ad1 = Adherent()
# ad1.lireDepuisClavier()
# ad1.enregistrerDansFichier()
# print("=====La liste des adérents=============")
# ad1.afficherListeAdherent()
# ad1.supprimerAdherent()



