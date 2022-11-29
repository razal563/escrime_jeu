from pynput import keyboard
import pygame
import time
from jeu import Jeu
from pygame import mixer
#initialisation de la matrice contenant les élements du jeu
#et initialisation de la classe JEU
#et du time.clock qui créer un objet pour faciliter le suivi du temps qui nous permettra de rafraichir notre matrice 60 fois par seconde

jeu = Jeu()
terminal = [[" " for i in range(jeu.longueur)] for j in range(jeu.hauteur)]
clock = pygame.time.Clock()
     
#Fonction qui permet de stocker le nom d'une fonction dans un tableau et donné une valeur à une variable pour pouvoir utilisé 2 touches
#en meme temps, elle est utilisé lors de l'attaque du joueur 2  
#Fais partit du 2ème listener 
#Permet de créer des actions lors de l'interractions avec les différentes touches du clavier
def on_release2(key):  
    if key == keyboard.KeyCode.from_char("o"):
        jeu.joueur2.mode_attaque2 = 1
        jeu.joueur2.inter_joueur_2.append(jeu.fonction_interract_attaque1_joueur_2)
        jeu.joueur2.inter_joueur_2.append(jeu.fonction_interract_attaque2_joueur_2)
        
#Fonction qui permet de stocker le nom d'une fonction dans un tableau et donné une valeur à une variable pour pouvoir utilisé 2 touches  
#en meme temps, elle est utilisé lors de la défense du joueur 2 
#Fais partit du 2ème listener   
#Permet de créer des actions lors de l'interractions avec les différentes touches du clavier   
def on_press2(key):
    if key == keyboard.KeyCode.from_char("p"):
        jeu.joueur2.mode_defense2 = 1
        jeu.joueur2.inter_joueur_2.append(jeu.fonction_interract_defense_joueur_2)

#Fonction qui permet de stocker le nom d'une fonction dans un tableau et donné une valeur à une variable pour pouvoir utilisé 2 touches  
#en meme temps, elle est utilisé lors de la défense du joueur 1   
#Permet de créer des actions lors de l'interractions avec les différentes touches du clavier    
#Elle fait partit du 1er listener 
def on_press(key):
    if key == keyboard.KeyCode.from_char("s"):
        jeu.joueur1.mode_defense1 = 1
        jeu.joueur1.inter_joueur_1.append(jeu.fonction_interract_defense_joueur_1)    
                              
#Fonction qui s'enclenche si une touche est relache et qu'elle est bien mentionné dedans sinon rien ne se passe
#Permet de créer des actions lors de l'interractions avec les différentes touches du clavier 
#Si le jeu est en pause on peut utiliser certaine touche mais pas toute  
#Elle fait partit du 1er listener
def on_release(key):
    if key == keyboard.Key.space:
        jeu.pause_menu = 1 
        mixer.init()
        mixer.music.load("zelda-main-theme-song.mp3")
        mixer.music.play(-1)
        jeu.pause_menu2(terminal)
    if jeu.pause_menu == 1:   
        if key == keyboard.Key.tab:
            if jeu.pause_menu == 1:
                jeu.pause_menu = 0 
                mixer.music.stop()
                jeu.reset2(terminal) 
            
        if key == keyboard.KeyCode.from_char("y"):
            if jeu.pause_menu == 1 and jeu.commande == 1:
                jeu.commande == 0
                jeu.effacer(terminal)
                    
        if key == keyboard.KeyCode.from_char("t"):       
            if jeu.pause_menu == 1:
                jeu.commande = 1
                jeu.options(terminal)  
                 
        if key == keyboard.KeyCode.from_char("x"):
            jeu.quitter = 1
                
    else:
        if key == keyboard.KeyCode.from_char("x"):
            jeu.quitter = 1  
               
        if key == keyboard.KeyCode.from_char("d"):
            mixer.init()
            mixer.music.load("sfx_step_grass_l.mp3")
            mixer.music.set_volume(.1)
            mixer.music.play(-1)
            jeu.joueur1.supprimer_avancer_joueur1(terminal,jeu.hauteur,jeu.joueur2.coord2)
            jeu.joueur1.avancer_reculer1(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            time.sleep(1/3)
            mixer.music.stop()
            
        if key == keyboard.KeyCode.from_char("z"):
            jeu.joueur1.mode_attaque1 = 1
            jeu.joueur1.inter_joueur_1.append(jeu.fonction_interract_attaque1_joueur_1)
            jeu.joueur1.inter_joueur_1.append(jeu.fonction_interract_attaque2_joueur_1)  
              
        if key == keyboard.KeyCode.from_char("q"):
            mixer.init()
            mixer.music.load("sfx_step_grass_l.mp3")
            mixer.music.set_volume(.1)
            mixer.music.play(-1)
            jeu.joueur1.supprimer_reculer_joueur1(terminal,jeu.hauteur)
            jeu.joueur1.avancer_reculer1(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            time.sleep(1/3)
            mixer.music.stop()
        
        if key == keyboard.KeyCode.from_char("e"):
            jeu.joueur1.supprimer_sauter1(terminal,jeu.hauteur)
            jeu.joueur1.sauter1(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            jeu.joueur1.supprimer_avancer_sauter_droite1(terminal,jeu.hauteur,jeu.joueur2.coord2)
            jeu.joueur1.sauter1(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            jeu.joueur1.supprimer_sauter_avancer1(terminal,jeu.hauteur)
            if(jeu.joueur1.res == 1):
                jeu.joueur1.supprimer_avancer_sauter_gauche1(terminal,jeu.hauteur)
                jeu.joueur1.sauter1(terminal,jeu.hauteur,jeu.fps)
                jeu.clear()
                jeu.affichage(terminal)
                jeu.joueur1.supprimer_sauter_avancer1(terminal,jeu.hauteur)
                jeu.joueur1.res = 0 
            jeu.joueur1.avancer_reculer1(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
    
        if key == keyboard.KeyCode.from_char("a"):
            jeu.joueur1.supprimer_sauter1(terminal,jeu.hauteur)
            jeu.joueur1.sauter1(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            jeu.joueur1.supprimer_avancer_sauter_gauche1(terminal,jeu.hauteur)
            jeu.joueur1.sauter1(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            jeu.joueur1.supprimer_sauter_reculer2(terminal,jeu.hauteur)
            if(jeu.joueur1.res == 1):
                jeu.joueur1.supprimer_avancer_sauter_gauche1(terminal,jeu.hauteur)
                jeu.joueur1.sauter1(terminal,jeu.hauteur,jeu.fps)
                jeu.clear()
                jeu.affichage(terminal)
                jeu.joueur1.supprimer_sauter_reculer2(terminal,jeu.hauteur)
                jeu.joueur1.res = 0   
            jeu.joueur1.avancer_reculer1(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
        
        if key == keyboard.KeyCode.from_char("m"):
            jeu.joueur2.supprimer_sauter2(terminal,jeu.hauteur)
            jeu.joueur2.sauter2(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            jeu.joueur2.supprimer_avancer_sauter_droite2(terminal,jeu.hauteur)
            jeu.joueur2.sauter2(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            jeu.joueur2.supprimer_sauter_avancer3(terminal,jeu.hauteur)
            if(jeu.joueur2.k == 1):
                jeu.joueur2.supprimer_avancer_sauter_droite2(terminal,jeu.hauteur)
                jeu.joueur2.sauter2(terminal,jeu.hauteur,jeu.fps)
                jeu.clear()
                jeu.affichage(terminal)
                jeu.joueur2.supprimer_sauter_avancer3(terminal,jeu.hauteur)
                jeu.joueur2.k = 0
            jeu.joueur2.avancer_reculer2(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)  
        
        if key == keyboard.KeyCode.from_char("l"):
            jeu.joueur2.supprimer_sauter2(terminal,jeu.hauteur)
            jeu.joueur2.sauter2(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            jeu.joueur2.supprimer_avancer_sauter_gauche2(terminal,jeu.hauteur,jeu.joueur1.coord)
            jeu.joueur2.sauter2(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            jeu.joueur2.supprimer_sauter_reculer(terminal,jeu.hauteur)
            if(jeu.joueur2.k == 1):
                jeu.joueur2.supprimer_avancer_sauter_gauche2(terminal,jeu.hauteur,jeu.joueur1.coord)
                jeu.joueur2.sauter2(terminal,jeu.hauteur,jeu.fps)
                jeu.clear()
                jeu.affichage(terminal)
                jeu.joueur2.supprimer_sauter_reculer(terminal,jeu.hauteur)
                jeu.joueur2.k = 0
            jeu.joueur2.avancer_reculer2(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal) 
              
        if key == keyboard.Key.right:
            mixer.init()
            mixer.music.load("sfx_step_grass_l.mp3")
            mixer.music.set_volume(.1)
            mixer.music.play(-1)
            jeu.joueur2.supprimer_reculer_joueur2(terminal,jeu.hauteur)
            jeu.joueur2.avancer_reculer2(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal)
            time.sleep(1/3)
            mixer.music.stop()
        
        if key == keyboard.Key.left:
            mixer.init()
            mixer.music.load("sfx_step_grass_l.mp3")
            mixer.music.set_volume(.1)
            mixer.music.play(-1)
            jeu.joueur2.supprimer_avancer_joueur2(terminal,jeu.hauteur,jeu.joueur1.coord)
            jeu.joueur2.avancer_reculer2(terminal,jeu.hauteur,jeu.fps)
            jeu.clear()
            jeu.affichage(terminal) 
            time.sleep(1/3)
            mixer.music.stop()
            
            
                 
#Initialisation de la scene de jeux en ajoutant dans la matrice
#la scene, les joueurs et le score 
#Et ensuite affiche la matrice      
jeu.scene(terminal)
jeu.joueur1.joueur_1(terminal,jeu.hauteur)
jeu.joueur2.joueur_2(terminal,jeu.hauteur)
jeu.obstacle_1(terminal)
jeu.score(terminal)
jeu.ligne(terminal)
jeu.affichage(terminal)

#Le listener est lis l'interraction des touches tant que le programme n'est pas terminé
#Ils sont appelés directement à partir de thread
#C'est pour cela que l'on doit attendre que qu'une action se finisse pour que l'autre débute
listener = keyboard.Listener( on_press=on_press,on_release=on_release)
listener.start()

listener2 = keyboard.Listener( on_press=on_press2,on_release=on_release2)
listener2.start()      

#Tant que les joueurs n'ont pas appuyé sur la touche x pour quitter le jeu alors 
#la matrice se rafraichis toutes les 60 fois par secondes
#et on verifie si nous ne sommes pas dans des états importants du jeu 
while(jeu.quitter2() != True):
    clock.tick(jeu.fps)
    jeu.attaque_meme_temps(terminal)    
    
    for i in jeu.joueur1.inter_joueur_1:
        i(terminal)
        del jeu.joueur1.inter_joueur_1[0]
        
    for i in jeu.joueur2.inter_joueur_2:
        i(terminal)
        del jeu.joueur2.inter_joueur_2[0]
        
    jeu.defense_attaque(terminal)
    jeu.attaque_defense(terminal)