#Cette classe est presque la meme que celle de la version terminale mais nettement plus simple
#On initialise des variables qui nous aident au bon fonctionnement du jeu
#Elle fais appelle au classe joueur1 et joueur2
import pygame
from joueur1 import Joueur1
from joueur2 import Joueur2
from pygame import mixer

class Jeu:
    #Initialisation de la classe jeu
    def __init__(self):
        self.pause = False
        self.joueur1 = Joueur1()  
        self.joueur2 = Joueur2()
        self.attaque_range = 90
        self.width = 1020
        self.height = 500
        self.menu_pause = "pause"
        self.run = True
        self.presser = {}
    
    #restart le jeu     
    def restart(self):
        self.joueur1.rect.x = 100
        self.joueur1.rect.y = 200
        self.joueur2.rect.x =  750
        self.joueur2.rect.y = 200
        
    #Cette fonction est utilisé lors du menu pause 
    #Elle fait aussi appelle au bouton
    #Certaine des fonction utilisé permettent d'ecrire sur le background 
    #Notamment pour afficher les commandes du jeu au joueur     
    def pause2(self,boutton1,boutton2,boutton3,boutton4,screen):
        if self.menu_pause == "pause":
            if boutton1.draw(screen):
                self.pause = False
                mixer.music.stop()
            if boutton2.draw(screen):
                self.run = False
            if boutton3.draw(screen):
                self.menu_pause = "commande"
        if self.menu_pause == "commande":
            myfont = pygame.font.SysFont("aerial", 50) 
            touche = myfont.render("Comment Jouer ? ", 1, (0,0,0))
            screen.blit(touche, (350, 15))
            myfont2 = pygame.font.SysFont("aerial", 35)
            #joueur1
            touche1 = myfont2.render("Joueur à gauche", 1, (0,0,0))
            screen.blit(touche1, (200, 70))
            touche2 = myfont2.render("Avancer: d ", 1, (0,0,0))
            screen.blit(touche2, (200, 110))
            touche3 = myfont2.render("Reculer: q ", 1, (0,0,0))
            screen.blit(touche3, (200, 150))
            touche4 = myfont2.render("Sauter à droite: e ", 1, (0,0,0))
            screen.blit(touche4, (200, 190))
            touche5 = myfont2.render("Sauter à gauche: a ", 1, (0,0,0))
            screen.blit(touche5, (200, 230))
            touche6 = myfont2.render("Attaquer: z ", 1, (0,0,0))
            screen.blit(touche6, (200, 270))
            touche7 = myfont2.render("Défendre: s ", 1, (0,0,0))
            screen.blit(touche7, (200, 310))
            #joueur2
            touche1 = myfont2.render("Joueur à droite", 1, (0,0,0))
            screen.blit(touche1, (550, 70))
            touche2 = myfont2.render("Avancer: fleche droite ", 1, (0,0,0))
            screen.blit(touche2, (550, 110))
            touche3 = myfont2.render("Reculer: fleche gauche ", 1, (0,0,0))
            screen.blit(touche3, (550, 150))
            touche4 = myfont2.render("Sauter à droite: m ", 1, (0,0,0))
            screen.blit(touche4, (550, 190))
            touche5 = myfont2.render("Sauter à gauche: l ", 1, (0,0,0))
            screen.blit(touche5, (550, 230))
            touche6 = myfont2.render("Attaquer: o ", 1, (0,0,0))
            screen.blit(touche6, (550, 270))
            touche7 = myfont2.render("Défendre: p ", 1, (0,0,0))
            screen.blit(touche7, (550, 310))
            if boutton4.draw(screen):
                self.menu_pause = "pause" 
        
    