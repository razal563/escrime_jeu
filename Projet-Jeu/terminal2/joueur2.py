#Dans cette classe sont implementée des fonctions qui servent pour les déplacements du joueur2, de l'attaque, 
#de la défense, mais aussi des collisions avec le joueur1 et les objets 
#Il y a aussi les time.sleep qui servent à savoir à quelle "vitesse" mon personnage vas avancer,reculer,sauter,attaquer ou défendre
import time 

class Joueur2:
    
    def __init__(self):
        self.coord2 = 0
        self.mouvement_speed = 5
        self.attaque_speed = 1
        self.block_time = 1
        self.mode_attaque2 = 0
        self.mode_defense2 = 0
        self.attaque_range = 1
        self.defense_range = 5
        self.score2 = 0
        self.k = 0
        self.inter_joueur_2 = []
        
    #Ajouter le joueurs 2
    def joueur_2(self,matrice,h):        
        for i in range(h):
            if i == h - 6:
                matrice[i][self.coord2] = "<o>"
            if i == h - 5:
                matrice[i][self.coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"
            if i == h - 4:
                matrice[i][self.coord2+3] = "|"
            if i == h - 3:
                matrice[i][self.coord2+3] = "|"
            if i == h - 2:
                matrice[i][self.coord2+2] = "|\ "
                
    #Supprimer le joueur2 de la matrice lorsqu'il recule
    def supprimer_reculer_joueur2(self,matrice,h):
        if(self.coord2 < 95):
            if(matrice[h-2][self.coord2+4] == "x"):
                matrice[h-6][self.coord2] = " "
                matrice[h-5][self.coord2-1] = " "
                matrice[h-4][self.coord2+3] = " "
                matrice[h-3][self.coord2+3] = " "
                matrice[h-2][self.coord2+2] = " "
                self.coord2 = self.coord2
            else:
                matrice[h-6][self.coord2] = " "
                matrice[h-5][self.coord2-1] = " "
                matrice[h-4][self.coord2+3] = " "
                matrice[h-3][self.coord2+3] = " "
                matrice[h-2][self.coord2+2] = " "
                self.coord2 = self.coord2 + 1 
        else: 
            matrice[h-6][self.coord2] = " "
            matrice[h-5][self.coord2-1] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+3] = " "
            matrice[h-2][self.coord2+2] = " "
            self.coord2 = 90  
            
    #Supprimer le joueur2 de la matrice lorsqu'il avance  
    def supprimer_avancer_joueur2(self,matrice,h,coord):
        if(self.coord2 > coord + 3):
            if(matrice[h-2][self.coord2-1] == "x"):
                matrice[h-6][self.coord2] = " "
                matrice[h-5][self.coord2-1] = " "
                matrice[h-4][self.coord2+3] = " "
                matrice[h-3][self.coord2+3] = " "
                matrice[h-2][self.coord2+2] = " "
                self.coord2 = self.coord2 
            else:
                matrice[h-6][self.coord2] = " "
                matrice[h-5][self.coord2-1] = " "
                matrice[h-4][self.coord2+3] = " "
                matrice[h-3][self.coord2+3] = " "
                matrice[h-2][self.coord2+2] = " "
                self.coord2 = self.coord2 - 1  
        
    #Fonction avancer et reculer le joueur2
    def avancer_reculer2(self,matrice,h,fps):
        time.sleep(self.mouvement_speed/fps)
        matrice[h-6][self.coord2] = "<o>"
        matrice[h-5][self.coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"
        matrice[h-4][self.coord2+3] = "|"
        matrice[h-3][self.coord2+3] = "|"
        matrice[h-2][self.coord2+2] = "|" + chr(92) 
    
    #Supprime la position de depart du joueur 2
    def supprimer_sauter2(self,matrice,h):   
        matrice[h-6][self.coord2] = " "
        matrice[h-5][self.coord2-1] = " "
        matrice[h-4][self.coord2+3] = " "
        matrice[h-3][self.coord2+3] = " "
        matrice[h-2][self.coord2+2] = " "

    #Supprime la position de reculement lors du saut du joueur 2   
    def supprimer_sauter_reculer(self,matrice,h):
        if (matrice[h-2][self.coord2+2] == "x"):
            matrice[h-7][self.coord2+2] = " "
            matrice[h-6][self.coord2-1] = " "
            matrice[h-5][self.coord2+1] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+3] = " " 
            self.coord2 = self.coord2 - 3
            self.k = 1
        else:
            matrice[h-7][self.coord2+2] = " "
            matrice[h-6][self.coord2-1] = " "
            matrice[h-5][self.coord2+1] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+3] = " " 
            
    #Supprime la position d'avancement lors du saut du joueur 2   
    def supprimer_sauter_avancer3(self,matrice,h):
        if(matrice[h-2][self.coord2+3] == "x"):
            matrice[h-7][self.coord2+2] = " "
            matrice[h-6][self.coord2-1] = " "
            matrice[h-5][self.coord2+1] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+3] = " " 
            self.coord2 = self.coord2 + 3
            self.k = 1
        else:
            matrice[h-7][self.coord2+2] = " "
            matrice[h-6][self.coord2-1] = " "
            matrice[h-5][self.coord2+1] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+3] = " " 
    
    #Supprime le saut a droite du joueur 2   
    def supprimer_avancer_sauter_droite2(self,matrice,h):
        if(self.coord2 < 95):
            matrice[h-7][self.coord2+2] = " "
            matrice[h-6][self.coord2-1] = " "
            matrice[h-5][self.coord2+1] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+3] = " "
            self.coord2 = self.coord2 + 1 
        
        else: 
            matrice[h-7][self.coord2] = " "
            matrice[h-6][self.coord2-1] = " "
            matrice[h-5][self.coord2+3] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+2] = " " 
            self.coord2 = 90

    #Supprime le saut a gauche du joueur 1 
    def supprimer_avancer_sauter_gauche2(self,matrice,h,coord):
        if(self.coord2 > coord + 3):
            matrice[h-7][self.coord2+2] = " "
            matrice[h-6][self.coord2-1] = " "
            matrice[h-5][self.coord2+1] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+3] = " "
            self.coord2 = self.coord2 - 1 
        
        else: 
            matrice[h-7][self.coord2] = " "
            matrice[h-6][self.coord2-1] = " "
            matrice[h-5][self.coord2+3] = " "
            matrice[h-4][self.coord2+3] = " "
            matrice[h-3][self.coord2+2] = " "
            self.coord2 = coord + 3
        
    #Fonction qui fais sauter le joueur 2
    def sauter2(self,matrice,h,fps):
        time.sleep(self.mouvement_speed/fps)
        matrice[h-7][self.coord2+2] = "<o>"
        matrice[h-6][self.coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"
        matrice[h-5][self.coord2+1] = "|"
        matrice[h-4][self.coord2+3] = "|"
        matrice[h-3][self.coord2+3] = "|" + chr(92)
        
    #Fonction qui supprime le states qui a eu lui du joueur 2
    def supprimer_states2(self,matrice,h):
        matrice[h-5][self.coord2-1] = " " 
    
    #Rétablir le states precedent du joueur 2
    def rétablir_states2(self,matrice,h):
        matrice[h-5][self.coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"

    #Fonction qui declenche l'attaque pour le joueur 2
    def attaquer2(self,matrice,h,fps):
        time.sleep(self.attaque_speed/fps)
        matrice[h-5][self.coord2-1] = "\033[1;31;40m" + "-" +"\033[0;0;0m" + "-|" 
        
    #Fonction qui declenche la défence pour le joueur 2  
    def defense2(self,matrice,h,fps):
        time.sleep(self.block_time/fps)
        matrice[h-5][self.coord2-1] =  "\033[1;31;40m" + "|" +"\033[0;0;0m" + "_|"
        
