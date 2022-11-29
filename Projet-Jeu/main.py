from os import system, name
import pynput
from pynput import keyboard
import time
import pygame

#Initialisation de la taille de notre "interface" de jeu
#Et initialisation de la matrice contenant les élements du jeu
#Initialisation des variables globales
hauteur = 11
longueur = 100
terminal = [[" " for i in range(longueur)] for j in range(hauteur)]
inter_joueur_1 = []
inter_joueur_2 = []
k = 0
coord = 0
coord2 = 0
obstacle = 0
fps = 80
clock = pygame.time.Clock()
mouvement_speed = 5
attaque_speed = 1
block_time = 1
mode_attaque1 = 0
mode_attaque2 = 0
mode_defense1 = 0
mode_defense2 = 0
attaque_range = 1
defense_range = 5
block_time = 1
score1 = 0
score2 = 0


def clear():
    #pour windows
    if name == 'nt':
        _ = system('cls')
    #pour mac et linux
    else:
        _ = system('clear')

#Création de la Scene à partir du fichier scene
def scene(matrice,h,l):
    res = []
    res2 = 0
    with open("scene.ffscene", "r") as my_file:
        f = my_file.read()
        for i in f:
            res.append(i)
    for m in res:
        if (m == "x"):
            global obstacle
            obstacle = res.index(m)*10
        elif (m == '1'):
            global coord
            coord = res.index(m)*10
        elif (m == '2'):
            global coord2
            coord2 = res.index(m)*10
        else:
            res2 = m
    for j in range(l):
        matrice[h-1][j] = res2

#Ajouter le joueurs 1
def joueur_1(matrice,h,l,x):
    for i in range(h):
        if i == h - 6:
            matrice[i][x] = "<o>"
        if i == h - 5:
            matrice[i][x+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
        if i == h - 4:
            matrice[i][x+1] = "|"
        if i == h - 3:
            matrice[i][x+1] = "|"
        if i == h - 2:
            matrice[i][x] = "/|"
        
#Ajouter le joueurs 2
def joueur_2(matrice,h,l,y):        
    for i in range(h):
        if i == h - 6:
            matrice[i][y] = "<o>"
        if i == h - 5:
            matrice[i][y-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"
        if i == h - 4:
            matrice[i][y+3] = "|"
        if i == h - 3:
            matrice[i][y+3] = "|"
        if i == h - 2:
            matrice[i][y+2] = "|\ "

#Ajouter les obstacle
def obstacle_1(matrice,h,z):
    matrice[h-2][z] = "x"
    
#Affichage du Score
def score(matrice,h,l,x,y):
    for i in range(h):
        if i == h - 10:
            matrice[i][int(l/2)] = "|"
            matrice[i][int(l/2)-1] = x
            matrice[i][int(l/2)-2] = "|"
            matrice[i][int(l/2)+1] = y
            matrice[i][int(l/2)+2] = "|"
        
#Affichage de la ligne 
def ligne(matrice,l):
    for i in range(l):
        matrice[0][i] = "-"     
    
#Affichage de la matrice 
def affichage(matrice):
    for i in terminal:
        for j in i:
            print(j,end='')
        print('')
        
#Fonction pour quitter le jeu      
def quitter(i):
    if i == 1:
        return True
    else:
        return False
    
#Fonction quand une touche est relache enclenche quelque chose   
def on_release2(key): 
    global mode_attaque2 
    if key == keyboard.KeyCode.from_char("o"):
        mode_attaque2 = 1
        inter_joueur_2.append(fonction_interract_attaque1_joueur_2)
        inter_joueur_2.append(fonction_interract_attaque2_joueur_2)
    
def on_press2(key):
    global mode_defense2
    if key == keyboard.KeyCode.from_char("p"):
        mode_defense2 = 1
        inter_joueur_2.append(fonction_interract_defense_joueur_2)
        
def on_press(key):
    global mode_defense1
    if key == keyboard.KeyCode.from_char("s"):
        mode_defense1 = 1
        inter_joueur_1.append(fonction_interract_defense_joueur_1)    
                              
#Fonction quand une touche est relache enclenche quelque chose   
def on_release(key):
    global score1,score2,mode_attaque1,mode_defense1
    if key == keyboard.KeyCode.from_char("x"):
        global k
        k = 1  
               
    if key == keyboard.KeyCode.from_char("d"):
        supprimer_avancer_joueur1(terminal,hauteur)
        avancer_reculer1(terminal,hauteur)
        clear()
        affichage(terminal)
            
    if key == keyboard.KeyCode.from_char("z"):
        mode_attaque1 = 1
        inter_joueur_1.append(fonction_interract_attaque1_joueur_1)
        inter_joueur_1.append(fonction_interract_attaque2_joueur_1)  
              
    if key == keyboard.KeyCode.from_char("q"):
        supprimer_reculer_joueur1(terminal,hauteur)
        avancer_reculer1(terminal,hauteur)
        clear()
        affichage(terminal)
        
    if key == keyboard.KeyCode.from_char("e"):
        supprimer_sauter1(terminal,hauteur)
        sauter1(terminal,hauteur)
        clear()
        affichage(terminal)
        supprimer_avancer_sauter_droite1(terminal,hauteur)
        sauter1(terminal,hauteur)
        clear()
        affichage(terminal)
        supprimer_sauter_avancer1(terminal,hauteur)
        avancer_reculer1(terminal,hauteur)
        clear()
        affichage(terminal)
    
    if key == keyboard.KeyCode.from_char("a"):
        supprimer_sauter1(terminal,hauteur)
        sauter1(terminal,hauteur)
        clear()
        affichage(terminal)
        supprimer_avancer_sauter_gauche1(terminal,hauteur)
        sauter1(terminal,hauteur)
        clear()
        affichage(terminal)
        supprimer_sauter_avancer1(terminal,hauteur)
        avancer_reculer1(terminal,hauteur)
        clear()
        affichage(terminal)
        
    if key == keyboard.KeyCode.from_char("m"):
        supprimer_sauter2(terminal,hauteur)
        sauter2(terminal,hauteur)
        clear()
        affichage(terminal)
        supprimer_avancer_sauter_droite2(terminal,hauteur)
        sauter2(terminal,hauteur)
        clear()
        affichage(terminal)
        supprimer_sauter_avancer2(terminal,hauteur)
        avancer_reculer2(terminal,hauteur)
        clear()
        affichage(terminal)  
        
    if key == keyboard.KeyCode.from_char("l"):
        supprimer_sauter2(terminal,hauteur)
        sauter2(terminal,hauteur)
        clear()
        affichage(terminal)
        supprimer_avancer_sauter_gauche2(terminal,hauteur)
        sauter2(terminal,hauteur)
        clear()
        affichage(terminal)
        supprimer_sauter_avancer2(terminal,hauteur)
        avancer_reculer2(terminal,hauteur)
        clear()
        affichage(terminal) 
              
    if key == keyboard.Key.right:
        supprimer_reculer_joueur2(terminal,hauteur)
        avancer_reculer2(terminal,hauteur)
        clear()
        affichage(terminal)
        
    if key == keyboard.Key.left:
        supprimer_avancer_joueur2(terminal,hauteur)
        avancer_reculer2(terminal,hauteur)
        clear()
        affichage(terminal)
        
#Supprimer le joueur 1 dans la matrice      
def supprimer_avancer_joueur1(matrice,h):
    global coord,coord2
    if(coord < coord2-3):
        matrice[h-6][coord] = " "
        matrice[h-5][coord+1] = " "
        matrice[h-4][coord+1] = " "
        matrice[h-3][coord+1] = " "
        matrice[h-2][coord] = " "
        coord = coord + 1 
        
#Supprimer le joueur2 dans la matrice  
def supprimer_reculer_joueur2(matrice,h):
    global coord2
    if(coord2 < 95):
        matrice[h-6][coord2] = " "
        matrice[h-5][coord2-1] = " "
        matrice[h-4][coord2+3] = " "
        matrice[h-3][coord2+3] = " "
        matrice[h-2][coord2+2] = " "
        coord2 = coord2 + 1 
        
    else: 
        matrice[h-6][coord2] = " "
        matrice[h-5][coord2-1] = " "
        matrice[h-4][coord2+3] = " "
        matrice[h-3][coord2+3] = " "
        matrice[h-2][coord2+2] = " "
        coord2 = 90  

#Supprimer le joueur2 dans la matrice  
def supprimer_avancer_joueur2(matrice,h):
    global coord2,coord
    if(coord2 > coord + 3):
        matrice[h-6][coord2] = " "
        matrice[h-5][coord2-1] = " "
        matrice[h-4][coord2+3] = " "
        matrice[h-3][coord2+3] = " "
        matrice[h-2][coord2+2] = " "
        coord2 = coord2 - 1  
        
#Supprimer le joueur 1 dans la matrice      
def supprimer_reculer_joueur1(matrice,h):
    global coord
    if(coord > 0):
        matrice[h-6][coord] = " "
        matrice[h-5][coord+1] = " "
        matrice[h-4][coord+1] = " "
        matrice[h-3][coord+1] = " "
        matrice[h-2][coord] = " "
        coord = coord - 1 
        
    else: 
        matrice[h-6][coord] = " "
        matrice[h-5][coord+1] = " "
        matrice[h-4][coord+1] = " "
        matrice[h-3][coord+1] = " "
        matrice[h-2][coord] = " "
        coord = 10         
                   
#Fonction avancer et reculer le joueur 1
def avancer_reculer1(matrice,h):
    global coord
    time.sleep(mouvement_speed/fps)
    matrice[h-6][coord] = "<o>"
    matrice[h-5][coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
    matrice[h-4][coord+1] = "|"
    matrice[h-3][coord+1] = "|"
    matrice[h-2][coord] = "/|" 

#Fonction avancer et reculer le joueur2
def avancer_reculer2(matrice,h):
    global coord2
    time.sleep(mouvement_speed/fps)
    matrice[h-6][coord2] = "<o>"
    matrice[h-5][coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"
    matrice[h-4][coord2+3] = "|"
    matrice[h-3][coord2+3] = "|"
    matrice[h-2][coord2+2] = "|" + chr(92)  

#Supprime la possition de depart du joueur 1
def supprimer_sauter1(matrice,h):
    global coord
    matrice[h-6][coord] = " "
    matrice[h-5][coord+1] = " "
    matrice[h-4][coord+1] = " "
    matrice[h-3][coord+1] = " "
    matrice[h-2][coord] = " " 
    
#Supprime la possition de depart du joueur 2
def supprimer_sauter2(matrice,h):   
    global coord2
    matrice[h-6][coord2] = " "
    matrice[h-5][coord2-1] = " "
    matrice[h-4][coord2+3] = " "
    matrice[h-3][coord2+3] = " "
    matrice[h-2][coord2+2] = " "
    
#Supprime la possition d'avancement lors du saut du joueur 1    
def supprimer_sauter_avancer1(matrice,h):
    global coord
    matrice[h-7][coord] = " "
    matrice[h-6][coord+1] = " "
    matrice[h-5][coord+1] = " "
    matrice[h-4][coord+1] = " "
    matrice[h-3][coord] = " "
    
#Supprime la possition d'avancement lors du saut du joueur 2   
def supprimer_sauter_avancer2(matrice,h):
    global coord2
    matrice[h-7][coord2+2] = " "
    matrice[h-6][coord2-1] = " "
    matrice[h-5][coord2+1] = " "
    matrice[h-4][coord2+3] = " "
    matrice[h-3][coord2+3] = " "     
    
#Supprime le saut a droite du joueur 1    
def supprimer_avancer_sauter_droite1(matrice,h):
    global coord
    if(coord < coord2 - 4):
        matrice[h-7][coord] = " "
        matrice[h-6][coord+1] = " "
        matrice[h-5][coord+1] = " "
        matrice[h-4][coord+1] = " "
        matrice[h-3][coord] = " "
        coord = coord + 1 
        
    else: 
        matrice[h-7][coord] = " "
        matrice[h-6][coord+1] = " "
        matrice[h-5][coord+1] = " "
        matrice[h-4][coord+1] = " "
        matrice[h-3][coord] = " "
        coord = coord2 - 4
        
#Supprime le saut a droite du joueur 2   
def supprimer_avancer_sauter_droite2(matrice,h):
    global coord2
    if(coord2 < 98):
        matrice[h-7][coord2+2] = " "
        matrice[h-6][coord2-1] = " "
        matrice[h-5][coord2+1] = " "
        matrice[h-4][coord2+3] = " "
        matrice[h-3][coord2+3] = " "
        coord2 = coord2 + 1 
        
    else: 
        matrice[h-7][coord2] = " "
        matrice[h-6][coord2-1] = " "
        matrice[h-5][coord2+3] = " "
        matrice[h-4][coord2+3] = " "
        matrice[h-3][coord2+2] = " " 
        coord2 = 90 
            
#Supprime le saut a gauche du joueur 1 
def supprimer_avancer_sauter_gauche1(matrice,h):
    global coord
    if(coord > 0):
        matrice[h-7][coord] = " "
        matrice[h-6][coord+1] = " "
        matrice[h-5][coord+1] = " "
        matrice[h-4][coord+1] = " "
        matrice[h-3][coord] = " "
        coord = coord - 1 
        
    else: 
        matrice[h-7][coord] = " "
        matrice[h-6][coord+1] = " "
        matrice[h-5][coord+1] = " "
        matrice[h-4][coord+1] = " "
        matrice[h-3][coord] = " "
        coord = 10 
   
#Supprime le saut a gauche du joueur 1 
def supprimer_avancer_sauter_gauche2(matrice,h):
    global coord2
    if(coord2 > coord + 3):
        matrice[h-7][coord2+2] = " "
        matrice[h-6][coord2-1] = " "
        matrice[h-5][coord2+1] = " "
        matrice[h-4][coord2+3] = " "
        matrice[h-3][coord2+3] = " "
        coord2 = coord2 - 1 
        
    else: 
        matrice[h-7][coord2] = " "
        matrice[h-6][coord2-1] = " "
        matrice[h-5][coord2+3] = " "
        matrice[h-4][coord2+3] = " "
        matrice[h-3][coord2+2] = " "
        coord2 = coord + 3       
        
#Fonction qui fais sauter le joueur 1
def sauter1(matrice,h):
    global coord 
    time.sleep(mouvement_speed/fps)
    matrice[h-7][coord] = "<o>"
    matrice[h-6][coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
    matrice[h-5][coord+1] = "|"
    matrice[h-4][coord+1] = "|"
    matrice[h-3][coord] = "/|"  
    
#Fonction qui fais sauter le joueur 2
def sauter2(matrice,h):
    global coord2 
    time.sleep(mouvement_speed/fps)
    matrice[h-7][coord2+2] = "<o>"
    matrice[h-6][coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"
    matrice[h-5][coord2+1] = "|"
    matrice[h-4][coord2+3] = "|"
    matrice[h-3][coord2+3] = "|" + chr(92)

#Fonction qui supprime le states qui a eu lui du joueur 1
def supprimer_states1(matrice,h):
    matrice[h-5][coord+1] = " " 
    
#Rétablir le states precedent 
def rétablir_states1(matrice,h):
    matrice[h-5][coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m" 
    
#Reset les joueurs 
def reset(matrice,h):
    global coord,coord2
    matrice[h-6][coord] = " "
    matrice[h-5][coord+1] = " "
    matrice[h-4][coord+1] = " "
    matrice[h-3][coord+1] = " "
    matrice[h-2][coord] = " " 
    
    matrice[h-6][coord2] = " "
    matrice[h-5][coord2-1] = " "
    matrice[h-4][coord2+3] = " "
    matrice[h-3][coord2+3] = " "
    matrice[h-2][coord2+2] = " "
    
    coord = 15
    coord2 = 80
    
    scene(terminal,hauteur,longueur)
    joueur_1(terminal,hauteur,longueur,coord)
    joueur_2(terminal,hauteur,longueur,coord2)
    obstacle_1(terminal,hauteur,obstacle)
    score(terminal,hauteur,longueur,score1,score2)
    ligne(terminal,longueur)
        
#Fonction qui declenche l'attaque pour le joueur 1
def attaquer1(matrice,h):
    global coord
    time.sleep(attaque_speed/fps)
    matrice[h-5][coord+1] =  "|-"+"\033[1;32;40m-\033[0;0;0m"  
   
#Fonction qui supprime le states qui a eu lui du joueur 2
def supprimer_states2(matrice,h):
    matrice[h-5][coord2-1] = " " 
    
#Rétablir le states precedent du joueur 2
def rétablir_states2(matrice,h):
    matrice[h-5][coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"

#Fonction qui declenche l'attaque pour le joueur 2
def attaquer2(matrice,h):
    global coord2
    time.sleep(attaque_speed/fps)
    matrice[h-5][coord2-1] = "\033[1;31;40m" + "-" +"\033[0;0;0m" + "-|"  
         
#Fonction qui declenche la défence pour le joueur 1   
def defense1(matrice,h):
    global coord 
    time.sleep(block_time/fps)
    matrice[h-5][coord+1] =  "|_"+"\033[1;32;40m|\033[0;0;0m" 
    
#Fonction qui declenche la défence pour le joueur 2  
def defense2(matrice,h):
    global coord2 
    time.sleep(block_time/fps)
    matrice[h-5][coord2-1] =  "\033[1;31;40m" + "|" +"\033[0;0;0m" + "_|"
    
# Fonction predefinie qui appelle d'autre fonction qui sont utilisé 
# pour pourvoir lancer l'attaque en meme temps lors de l'interraction
# simultane de 2 touches 
def fonction_interract_attaque1_joueur_1(matrice,h):
    supprimer_states1(matrice,h)
    attaquer1(matrice,h)
    clear()
    affichage(matrice) 
    
def fonction_interract_attaque1_joueur_2(matrice,h):
    if mode_defense1 == 0 :
        supprimer_states2(matrice,h)
        attaquer2(matrice,h)
        clear()
        affichage(matrice) 
    
def fonction_interract_attaque2_joueur_1(matrice,h):
    global score1,score2
    if ((coord2-1)-(coord+1) == attaque_range & (mode_defense2 == 0)):
        score1 +=1
        score(matrice,h,longueur,score1,score2)
        reset(matrice,h)
        clear()
        affichage(matrice)
    else:
        time.sleep(2/10)
        supprimer_states1(matrice,h)
        rétablir_states1(matrice,h)
        clear()
        affichage(matrice)   
    
def fonction_interract_attaque2_joueur_2(matrice,h):
    global score1,score2
    if ((coord2-1)-(coord+1) == attaque_range & (mode_defense1 == 0)):
        score2 +=1
        score(matrice,h,longueur,score1,score2)
        reset(matrice,h)
        clear()
        affichage(matrice)
    else:
        time.sleep(1/5)
        supprimer_states2(matrice,h)
        rétablir_states2(matrice,h)
        clear()
        affichage(matrice) 
        
def fonction_interract_defense_joueur_1(matrice,h):
    supprimer_states1(matrice,h)
    defense1(matrice,h)
    clear()
    affichage(matrice)
    time.sleep(1/5)
    supprimer_states1(matrice,h)
    rétablir_states1(matrice,h)
    clear()
    affichage(matrice)   
        
def fonction_interract_defense_joueur_2(matrice,h):
    supprimer_states2(matrice,h)
    defense2(matrice,h)
    clear()
    affichage(matrice)
    time.sleep(1/5)
    supprimer_states2(matrice,h)
    rétablir_states2(matrice,h)
    clear()
    affichage(matrice)   
                 
#Initialisation de la scene de jeux        
scene(terminal,hauteur,longueur)
joueur_1(terminal,hauteur,longueur,coord)
joueur_2(terminal,hauteur,longueur,coord2)
obstacle_1(terminal,hauteur,obstacle)
score(terminal,hauteur,longueur,score1,score2)
ligne(terminal,longueur)
affichage(terminal)

listener = keyboard.Listener( on_press=on_press,on_release=on_release)
listener.start()

listener2 = keyboard.Listener( on_press=on_press2,on_release=on_release2)
listener2.start()      
   
while(quitter(k) != True):
    clock.tick(fps)
    if (((coord2-1)-(coord+1) == attaque_range) & ( mode_attaque1 == 1 ) & (mode_attaque2 == 1)):
        reset(terminal,hauteur)
        clear()
        affichage(terminal)
        
    for i in inter_joueur_1:
        i(terminal,hauteur)
        del inter_joueur_1[0]
        
    for i in inter_joueur_2:
        i(terminal,hauteur)
        del inter_joueur_2[0]
        
    if (((coord2-1)-(coord+1) <= defense_range) & (mode_defense1 == 1) & (mode_attaque2 == 1)):
        terminal[hauteur-6][coord2] = " "
        terminal[hauteur-5][coord2+1] = " "
        terminal[hauteur-4][coord2+1] = " "
        terminal[hauteur-3][coord2+1] = " "
        terminal[hauteur-2][coord2] = " "
        coord2 = coord + 10
        terminal[hauteur-6][coord2] = "<o>"
        terminal[hauteur-5][coord2-1] = "\033[1;31;40m" + chr(92) +"\033[0;0;0m" + "_|"
        terminal[hauteur-4][coord2+3] = "|"
        terminal[hauteur-3][coord2+3] = "|"
        terminal[hauteur-2][coord2+2] = "|" + chr(92)
        obstacle_1(terminal,hauteur,obstacle)
        score(terminal,hauteur,longueur,score1,score2)
        clear()
        affichage(terminal)
        
    if (((coord2-1)-(coord+1) <= defense_range) & (mode_defense2 == 1) & (mode_attaque1 == 1)):
        terminal[hauteur-6][coord] = " "
        terminal[hauteur-5][coord+1] = " "
        terminal [hauteur-4][coord+1] = " "
        terminal[hauteur-3][coord+1] = " "
        terminal[hauteur-2][coord] = " "
        coord = coord2 - 10
        terminal[hauteur-6][coord] = "<o>"
        terminal[hauteur-5][coord+1] = "|_"+"\033[1;32;40m/\033[0;0;0m"
        terminal[hauteur-4][coord+1] = "|"
        terminal[hauteur-3][coord+1] = "|"
        terminal[hauteur-2][coord] = "/|" 
        obstacle_1(terminal,hauteur,obstacle)
        score(terminal,hauteur,longueur,score1,score2)
        clear()
        affichage(terminal)
        
    mode_attaque1 = 0  
    mode_attaque2 = 0     
    mode_defense1 = 0