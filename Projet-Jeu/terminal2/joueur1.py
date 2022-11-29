#Dans cette classe sont implementée des fonctions qui servent pour les déplacements du joueur1, de l'attaque, 
#de la défense, mais aussi des collisions avec le joueur2 et les objets 
#Il y a aussi les time.sleep qui servent à savoir à quelle "vitesse" mon personnage vas avancer,reculer,sauter,attaquer ou défendre
import time

class Joueur1:
    
    def __init__(self):
        self.coord = 0
        self.mouvement_speed = 5
        self.attaque_speed = 3
        self.block_time = 4
        self.mode_attaque1 = 0
        self.mode_defense1 = 0
        self.attaque_range = 1
        self.defense_range = 5
        self.score1 = 0
        self.res = 0
        self.inter_joueur_1 = []
        
    #Ajouter le joueurs 1
    def joueur_1(self,matrice,h):
        for i in range(h):
            if i == h - 6:
                matrice[i][self.coord] = "<o>"
            if i == h - 5:
                matrice[i][self.coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
            if i == h - 4:
                matrice[i][self.coord+1] = "|"
            if i == h - 3:
                matrice[i][self.coord+1] = "|"
            if i == h - 2:
                matrice[i][self.coord] = "/|"
                
    #Supprimer le joueur 1 de la matrice lorsqu'il avance      
    def supprimer_avancer_joueur1(self,matrice,h,coord2):
        if(self.coord < coord2-3):
            if(matrice[h-2][self.coord+2] == "x"):
                matrice[h-6][self.coord] = " "
                matrice[h-5][self.coord+1] = " "
                matrice[h-4][self.coord+1] = " "
                matrice[h-3][self.coord+1] = " "
                matrice[h-2][self.coord] = " "
                self.coord = self.coord 
            else:
                matrice[h-6][self.coord] = " "
                matrice[h-5][self.coord+1] = " "
                matrice[h-4][self.coord+1] = " "
                matrice[h-3][self.coord+1] = " "
                matrice[h-2][self.coord] = " "
                self.coord = self.coord + 1 
            
    #Supprimer le joueur 1 de la matrice lorsqu'il recule     
    def supprimer_reculer_joueur1(self,matrice,h):
        if(self.coord > 0):
            if(matrice[h-2][self.coord-2] == "x"):
                matrice[h-6][self.coord] = " "
                matrice[h-5][self.coord+1] = " "
                matrice[h-4][self.coord+1] = " "
                matrice[h-3][self.coord+1] = " "
                matrice[h-2][self.coord] = " "
                self.coord = self.coord 
            else:
                matrice[h-6][self.coord] = " "
                matrice[h-5][self.coord+1] = " "
                matrice[h-4][self.coord+1] = " "
                matrice[h-3][self.coord+1] = " "
                matrice[h-2][self.coord] = " "
                self.coord = self.coord - 1 
        
        else: 
            matrice[h-6][self.coord] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord+1] = " "
            matrice[h-2][self.coord] = " "
            self.coord = 10  
            
    #Fonction avancer et reculer le joueur 1
    def avancer_reculer1(self,matrice,h,fps):
        time.sleep(self.mouvement_speed/fps)
        matrice[h-6][self.coord] = "<o>"
        matrice[h-5][self.coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
        matrice[h-4][self.coord+1] = "|"
        matrice[h-3][self.coord+1] = "|"
        matrice[h-2][self.coord] = "/|" 

    #Supprime la position de depart du joueur 1
    def supprimer_sauter1(self,matrice,h):
        matrice[h-6][self.coord] = " "
        matrice[h-5][self.coord+1] = " "
        matrice[h-4][self.coord+1] = " "
        matrice[h-3][self.coord+1] = " "
        matrice[h-2][self.coord] = " " 
        
    #Supprime la position d'avancement lors du saut du joueur 1    
    def supprimer_sauter_avancer1(self,matrice,h):
        if(matrice[h-2][self.coord+1] == "x"):
            matrice[h-7][self.coord] = " "
            matrice[h-6][self.coord+1] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord] = " " 
            self.coord = self.coord + 4
            self.res = 1
        else:
            matrice[h-7][self.coord] = " "
            matrice[h-6][self.coord+1] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord] = " "
            
    #Supprime la position de reculement lors du saut du joueur 1    
    def supprimer_sauter_reculer2(self,matrice,h):
        if(matrice[h-2][self.coord-1] == "x"):
            matrice[h-7][self.coord] = " "
            matrice[h-6][self.coord+1] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord] = " " 
            self.coord = self.coord - 2
            self.res = 1
        else:
            matrice[h-7][self.coord] = " "
            matrice[h-6][self.coord+1] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord] = " "
        
    #Supprime le saut a droite du joueur 1    
    def supprimer_avancer_sauter_droite1(self,matrice,h,coord2):
        if(self.coord < coord2 - 4):
            matrice[h-7][self.coord] = " "
            matrice[h-6][self.coord+1] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord] = " "
            self.coord = self.coord + 1 
        
        else: 
            matrice[h-7][self.coord] = " "
            matrice[h-6][self.coord+1] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord] = " "
            self.coord = coord2 - 4
            
    #Supprime le saut a gauche du joueur 1 
    def supprimer_avancer_sauter_gauche1(self,matrice,h):
        if(self.coord > 0):
            matrice[h-7][self.coord] = " "
            matrice[h-6][self.coord+1] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord] = " "
            self.coord = self.coord - 1 
        
        else: 
            matrice[h-7][self.coord] = " "
            matrice[h-6][self.coord+1] = " "
            matrice[h-5][self.coord+1] = " "
            matrice[h-4][self.coord+1] = " "
            matrice[h-3][self.coord] = " "
            self.coord = 10 
            
    #Fonction qui fais sauter le joueur 1
    def sauter1(self,matrice,h,fps):
        time.sleep(self.mouvement_speed/fps)
        matrice[h-7][self.coord] = "<o>"
        matrice[h-6][self.coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
        matrice[h-5][self.coord+1] = "|"
        matrice[h-4][self.coord+1] = "|"
        matrice[h-3][self.coord] = "/|" 
        
    #Fonction qui supprime le states qui a eu lui du joueur 1
    def supprimer_states1(self,matrice,h):
        matrice[h-5][self.coord+1] = " " 
    
    #Rétablir le states precedent 
    def rétablir_states1(self,matrice,h):
        matrice[h-5][self.coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
        
    #Fonction qui declenche l'attaque pour le joueur 1
    def attaquer1(self,matrice,h,fps):
        time.sleep(self.attaque_speed/fps)
        matrice[h-5][self.coord+1] =  "|-"+"\033[1;32;40m-\033[0;0;0m"  
        
    #Fonction qui declenche la défence pour le joueur 1   
    def defense1(self,matrice,h,fps): 
        time.sleep(self.block_time/fps)
        matrice[h-5][self.coord+1] =  "|_"+"\033[1;32;40m|\033[0;0;0m"