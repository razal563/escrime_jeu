#Cette classe contient des fonctions qui sont lié à l'affichage du jeu, du score, des élements neccesaire au bon fonctionnement du jeu
#Dans cette classe nous definissons aussi des fonctions à éxécuter lorqu'il y a interraction de 2 touches en même temps   
import time
from joueur1 import Joueur1
from joueur2 import Joueur2
from os import system, name

class Jeu:
    #Initialisation des variables et des joueurs
    def __init__(self):
        self.pause = False
        self.joueur1 = Joueur1()  
        self.joueur2 = Joueur2()
        self.hauteur = 11
        self.longueur = 100
        self.fps = 80 #frame par seconde
        self.obstacle = []
        self.quitter = 0
        self.attaque_range = 1
        self.defense_range = 5
        self.pause_menu = 0
        self.commande = 0
        
    #Fonction clear qui permet de "nettoyer" le terminal
    def clear(self):
        #pour windows
        if name == 'nt':
            _ = system('cls')
        #pour mac et linux
        else:
            _ = system('clear')
    
    #Affichage de la matrice 
    def affichage(self,matrice):
        for i in matrice:
            for j in i:
                print(j,end='')
            print('')
    
    #Création de la Scene dans la matrice à partir du fichier scene
    def scene(self,matrice):
        res = []
        res2 = 0
        with open("scene.ffscene", "r") as my_file:
            f = my_file.read()
            for i in f:
                res.append(i)
        i = 0
        for m in res:
            i+=1
            if (m == "x"):
                self.obstacle.append(i*2)
                print(self.obstacle)
            elif (m == '1'):
                self.joueur1.coord = res.index(m)*2
            elif (m == '2'):
                self.joueur2.coord2 = res.index(m)*2
            else:
                res2 = m
        for j in range(self.longueur):
            matrice[self.hauteur-1][j] = res2
            
    #Ajouter les obstacle dans la matrice
    def obstacle_1(self,matrice):
        for i in self.obstacle:
            matrice[self.hauteur-2][i] = "x"
        
    #Affichage du Score dans la matrice
    def score(self,matrice):
        for i in range(self.hauteur):
            if i == self.hauteur - 10:
                matrice[i][int(self.longueur/2)] = "|"
                matrice[i][int(self.longueur/2)-1] = self.joueur1.score1
                matrice[i][int(self.longueur/2)-2] = "|"
                matrice[i][int(self.longueur/2)+1] = self.joueur2.score2
                matrice[i][int(self.longueur/2)+2] = "|"
        
    #Affichage de la ligne 
    def ligne(self,matrice):
        for i in range(self.longueur):
            matrice[0][i] = "-"     
        
    #Fonction pour quitter le jeu      
    def quitter2(self):
        if self.quitter == 1:
            return True
        else:
            return False
     
    #Reset des joueurs dans la matrice
    def reset(self,matrice):
        matrice[self.hauteur-6][self.joueur1.coord] = " "
        matrice[self.hauteur-5][self.joueur1.coord+1] = " "
        matrice[self.hauteur-4][self.joueur1.coord+1] = " "
        matrice[self.hauteur-3][self.joueur1.coord+1] = " "
        matrice[self.hauteur-2][self.joueur1.coord] = " " 
    
        matrice[self.hauteur-6][self.joueur2.coord2] = " "
        matrice[self.hauteur-5][self.joueur2.coord2-1] = " "
        matrice[self.hauteur-4][self.joueur2.coord2+3] = " "
        matrice[self.hauteur-3][self.joueur2.coord2+3] = " "
        matrice[self.hauteur-2][self.joueur2.coord2+2] = " "
    
        self.joueur1.coord = 15
        self.joueur2.coord2 = 80
    
        self.scene(matrice)
        self.joueur1.joueur_1(matrice,self.hauteur)
        self.joueur2.joueur_2(matrice,self.hauteur)
        self.obstacle_1(matrice)
        self.score(matrice)
        self.ligne(matrice)   
        
    # Fonction predefinie qui appelle d'autre fonction qui sont utilisé 
    # pour pourvoir lancer l'attaque en meme temps lors de l'interraction
    # simultane de 2 touches 
    def fonction_interract_attaque1_joueur_1(self,matrice):
        self.joueur1.supprimer_states1(matrice,self.hauteur)
        self.joueur1.attaquer1(matrice,self.hauteur,self.fps)
        self.clear()
        self.affichage(matrice) 
    
    def fonction_interract_attaque1_joueur_2(self,matrice):
        if self.joueur1.mode_defense1 == 0 :
            self.joueur2.supprimer_states2(matrice,self.hauteur)
            self.joueur2.attaquer2(matrice,self.hauteur,self.fps)
            self.clear()
            self.affichage(matrice) 
    
    def fonction_interract_attaque2_joueur_1(self,matrice):
        if ((self.joueur2.coord2-1)-(self.joueur1.coord+1) == self.attaque_range & (self.joueur2.mode_defense2 == 0)):
            self.joueur1.score1 +=1
            self.score(matrice)
            self.reset(matrice)
            self.clear()
            self.affichage(matrice)
        else:
            time.sleep(2/10)
            self.joueur1.supprimer_states1(matrice,self.hauteur)
            self.joueur1.rétablir_states1(matrice,self.hauteur)
            self.clear()
            self.affichage(matrice)   
    
    def fonction_interract_attaque2_joueur_2(self,matrice):
        if ((self.joueur2.coord2-1)-(self.joueur1.coord+1) == self.attaque_range & (self.joueur1.mode_defense1 == 0)):
            self.joueur2.score2 +=1
            self.score(matrice)
            self.reset(matrice)
            self.clear()
            self.affichage(matrice)
        else:
            time.sleep(1/5)
            self.joueur2.supprimer_states2(matrice,self.hauteur)
            self.joueur2.rétablir_states2(matrice,self.hauteur)
            self.clear()
            self.affichage(matrice) 
        
    def fonction_interract_defense_joueur_1(self,matrice):
        self.joueur1.supprimer_states1(matrice,self.hauteur)
        self.joueur1.defense1(matrice,self.hauteur,self.fps)
        self.clear()
        self.affichage(matrice)
        time.sleep(1/5)
        self.joueur1.supprimer_states1(matrice,self.hauteur)
        self.joueur1.rétablir_states1(matrice,self.hauteur)
        self.clear()
        self.affichage(matrice)   
        
    def fonction_interract_defense_joueur_2(self,matrice):
        self.joueur2.supprimer_states2(matrice,self.hauteur)
        self.joueur2.defense2(matrice,self.hauteur,self.fps)
        self.clear()
        self.affichage(matrice)
        time.sleep(1/5)
        self.joueur2.supprimer_states2(matrice,self.hauteur)
        self.joueur2.rétablir_states2(matrice,self.hauteur)
        self.clear()
        self.affichage(matrice) 
        
    #Fonction qui s'enclenche s'il y a attaque des 2 joueurs en meme temps 
    #Reset le jeu et donc la matrice
    def attaque_meme_temps(self,matrice):
        if (((self.joueur2.coord2-1)-(self.joueur1.coord+1) == self.attaque_range) & ( self.joueur1.mode_attaque1 == 1 ) & (self.joueur2.mode_attaque2 == 1)):
            self.reset(matrice)
            self.clear()
            self.affichage(matrice)
        self.joueur1.mode_attaque1 = 0  
        self.joueur2.mode_attaque2 = 0 
            
    #Fonction qui s'enclenche si le joueur2 attaque et le joueur1 defend
    #Elle modifie les coordonnées du joueur2
    def defense_attaque(self,matrice):
        if (((self.joueur2.coord2-1)-(self.joueur1.coord+1) <= self.defense_range) & (self.joueur1.mode_defense1 == 1) & (self.joueur2.mode_attaque2 == 1)):
            matrice[self.hauteur-6][self.joueur2.coord2] = " "
            matrice[self.hauteur-5][self.joueur2.coord2-1] = " "
            matrice[self.hauteur-4][self.joueur2.coord2+3] = " "
            matrice[self.hauteur-3][self.joueur2.coord2+3] = " "
            matrice[self.hauteur-2][self.joueur2.coord2+2] = " "
            self.joueur2.coord2 = self.joueur1.coord + 10
            matrice[self.hauteur-6][self.joueur2.coord2] = "<o>"
            matrice[self.hauteur-5][self.joueur2.coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"
            matrice[self.hauteur-4][self.joueur2.coord2+3] = "|"
            matrice[self.hauteur-3][self.joueur2.coord2+3] = "|"
            matrice[self.hauteur-2][self.joueur2.coord2+2] = "|" + chr(92)
            self.obstacle_1(matrice)
            self.score(matrice)
            self.clear()
            self.affichage(matrice)
        self.joueur2.mode_attaque2 = 0     
        self.joueur1.mode_defense1 = 0
            
    #Fonction qui s'enclenche si le joueur2 defend et le joueur1 attaque
    #Elle modifie les coordonnées du joueur1
    def attaque_defense(self,matrice):
        if (((self.joueur2.coord2-1)-(self.joueur1.coord+1) <= self.defense_range) & (self.joueur2.mode_defense2 == 1) & (self.joueur1.mode_attaque1 == 1)):
            matrice[self.hauteur-6][self.joueur1.coord] = " "
            matrice[self.hauteur-5][self.joueur1.coord+1] = " "
            matrice [self.hauteur-4][self.joueur1.coord+1] = " "
            matrice[self.hauteur-3][self.joueur1.coord+1] = " "
            matrice[self.hauteur-2][self.joueur1.coord] = " "
            self.joueur1.coord = self.joueur2.coord2 - 10
            matrice[self.hauteur-6][self.joueur1.coord] = "<o>"
            matrice[self.hauteur-5][self.joueur1.coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
            matrice[self.hauteur-4][self.joueur1.coord+1] = "|"
            matrice[self.hauteur-3][self.joueur1.coord+1] = "|"
            matrice[self.hauteur-2][self.joueur1.coord] = "/|" 
            self.obstacle_1(matrice)
            self.score(matrice)
            self.clear()
            self.affichage(matrice) 
        self.joueur2.mode_defense2 = 0
        self.joueur1.mode_attaque1 = 0 
        
    #Configure un menu pause lors de l'interraction avec la touche espace 
    #Efface les choses inutiles precedentes de la matrice et rajoute les choses qui seront utile pour le menu pause  
    def pause_menu2(self,matrice):
        #Supprime le score de la matrice
        matrice[self.hauteur - 10][int(self.longueur/2)] = " "
        matrice[self.hauteur - 10][int(self.longueur/2)-1] = " "
        matrice[self.hauteur - 10][int(self.longueur/2)-2] = " "
        matrice[self.hauteur - 10][int(self.longueur/2)+1] = " "
        matrice[self.hauteur - 10][int(self.longueur/2)+2] = " "
        #Supprime les obstacles de la matrice
        for i in self.obstacle:
            matrice[self.hauteur-2][i] = " "
        #Supprime le joueur1 de la matrice
        matrice[self.hauteur-6][self.joueur1.coord] = " "
        matrice[self.hauteur-5][self.joueur1.coord+1] = " "
        matrice [self.hauteur-4][self.joueur1.coord+1] = " "
        matrice[self.hauteur-3][self.joueur1.coord+1] = " "
        matrice[self.hauteur-2][self.joueur1.coord] = " "
        #Supprime le joueur2 de la matrice
        matrice[self.hauteur-6][self.joueur2.coord2] = " "
        matrice[self.hauteur-5][self.joueur2.coord2-1] = " "
        matrice[self.hauteur-4][self.joueur2.coord2+3] = " "
        matrice[self.hauteur-3][self.joueur2.coord2+3] = " "
        matrice[self.hauteur-2][self.joueur2.coord2+2] = " "
        #Rajouter les differentes fonctionnalités
        matrice[self.hauteur - 9][int(self.longueur/2 - 10 )] = "Quitter --> x"
        matrice[self.hauteur - 7][int(self.longueur/2 - 10)] = "Options --> t"
        matrice[self.hauteur - 5][int(self.longueur/2 - 10)] = "Back --> tab"
        self.clear()
        self.affichage(matrice)
        
    #Reset le jeu c'est à dire qu'on ne se trouve plus dans le menu_pause et que la pause est fini  
    def reset2(self,matrice):
        matrice[self.hauteur - 9][int(self.longueur/2 - 10 )] = " "
        matrice[self.hauteur - 7][int(self.longueur/2 - 10)] = " "
        matrice[self.hauteur - 5][int(self.longueur/2 - 10)] = " "
        self.joueur1.joueur_1(matrice,self.hauteur)
        self.joueur2.joueur_2(matrice,self.hauteur)
        self.obstacle_1(matrice)
        self.score(matrice)
        self.clear()
        self.affichage(matrice)
        
    #Transition entre le menu_pause et l'options qui affiche les commandes des joueurs  
    def options(self,matrice):
        #Supprimer le menu_pause
        matrice[self.hauteur - 9][int(self.longueur/2 - 10 )] = " "
        matrice[self.hauteur - 7][int(self.longueur/2 - 10)] = " "
        matrice[self.hauteur - 5][int(self.longueur/2 - 10)] = " " 
        self.clear()
        #Rajouter les options de commande
        #joueur1
        matrice[self.hauteur - 9][int(self.longueur/2 - 40)] = "Les Touches pour le joueur 1:"
        matrice[self.hauteur - 7][int(self.longueur/2 - 40)] = "Avancer --> d"
        matrice[self.hauteur - 6][int(self.longueur/2 - 40)] = "Réculer --> q" 
        matrice[self.hauteur - 5][int(self.longueur/2 - 40)] = "Saut à gauche --> a" 
        matrice[self.hauteur - 4][int(self.longueur/2 - 40)] = "Saut à droite --> e" 
        matrice[self.hauteur - 3][int(self.longueur/2 - 40)] = "Attaquer --> z" 
        matrice[self.hauteur - 2][int(self.longueur/2 - 40)] = "Défendre --> s" 
        #Touche en plus
        matrice[self.hauteur - 2][int(self.longueur/2 - 21)] = " Quitter --> x" 
        matrice[self.hauteur - 3][int(self.longueur/2 - 20)] = "Back --> y" 
        #joueur2
        matrice[self.hauteur - 9][int(self.longueur/2 - 11)] = "Les Touches pour le joueur 2:"
        matrice[self.hauteur - 7][int(self.longueur/2 + 5)] = "Avancer --> fleche_gauche"
        matrice[self.hauteur - 6][int(self.longueur/2 + 5)] = "Réculer --> fleche_droite" 
        matrice[self.hauteur - 5][int(self.longueur/2 - 1)] = "Saut à gauche --> l" 
        matrice[self.hauteur - 4][int(self.longueur/2 - 1)] = "Saut à droite --> m" 
        matrice[self.hauteur - 3][int(self.longueur/2 - 5)] = "Attaquer --> o" 
        matrice[self.hauteur - 2][int(self.longueur/2 - 9)] = "Défendre --> p" 
        self.clear()
        self.affichage(matrice)
        
    #Efface toute les choses inutiles dans la matrice pour faire un back proprement
    def effacer(self,matrice):
        #joueur1
        matrice[self.hauteur - 9][int(self.longueur/2 - 40)] = " "
        matrice[self.hauteur - 7][int(self.longueur/2 - 40)] = " "
        matrice[self.hauteur - 6][int(self.longueur/2 - 40)] = " " 
        matrice[self.hauteur - 5][int(self.longueur/2 - 40)] = " " 
        matrice[self.hauteur - 4][int(self.longueur/2 - 40)] = " " 
        matrice[self.hauteur - 3][int(self.longueur/2 - 40)] = " " 
        matrice[self.hauteur - 2][int(self.longueur/2 - 40)] = " " 
        #Touche en plus
        matrice[self.hauteur - 2][int(self.longueur/2 - 21)] = " " 
        matrice[self.hauteur - 3][int(self.longueur/2 - 20)] = " " 
        #joueur2
        matrice[self.hauteur - 9][int(self.longueur/2 - 11)] = " "
        matrice[self.hauteur - 7][int(self.longueur/2 + 5)] = " "
        matrice[self.hauteur - 6][int(self.longueur/2 + 5)] = " " 
        matrice[self.hauteur - 5][int(self.longueur/2 - 1)] = " " 
        matrice[self.hauteur - 4][int(self.longueur/2 - 1)] = " " 
        matrice[self.hauteur - 3][int(self.longueur/2 - 5)] = " " 
        matrice[self.hauteur - 2][int(self.longueur/2 - 9)] = " "
        self.pause_menu2(matrice)
        self.clear()
        self.affichage(matrice)
        
        
        















