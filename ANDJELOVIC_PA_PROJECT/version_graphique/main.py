import pygame
from jeu import Jeu
import boutton
from pygame import mixer

pygame.init()
               
#generer la fenentre de jeu
jeu = Jeu()
screen = pygame.display.set_mode((jeu.width, jeu.height))
pygame.display.set_caption("Jeu d'escrime")

#Charger des images de boutton et de background
background = pygame.image.load('image/background.png ')
back_image = pygame.image.load("image/button_back.png")
quitter_image = pygame.image.load("image/button_quit.png")
options_image = pygame.image.load("image/button_options.png")

#Initialise les bouttons grâce à la classe et les charge dans des variables
boutton_back = boutton.Boutton(450,100,back_image,1)
boutton_quitter = boutton.Boutton(452,200,quitter_image,1)
boutton_options = boutton.Boutton(416,300,options_image,1)
boutton_back2 = boutton.Boutton(450,400,back_image,1)

menu_pause = "main"

#Utilisation de time.clock qui créer un objet pour faciliter le suivi du temps qui nous permettra 
#de rafraichir notre matrice 60 fois par seconde
clock = pygame.time.Clock()
fps = 60

#La fonction blit permet de dessiner sur une surface, ici la fenetre, comme le compilateur lis linéairement le code
#Il est important de mettre d'abord le background et ensuite les joueur sinon les joueur seront derriere le background
while jeu.run:
    #Taux de rafraichissement par seconde
    clock.tick(fps)
    #Rajout du background
    screen.blit(background,(0,0)) 
    if jeu.pause == True:
        jeu.pause2(boutton_back,boutton_quitter,boutton_options,boutton_back2,screen)       
    else:
        #Rajout du score sur le background du jeu
        myfont = pygame.font.SysFont("monospace", 50)
        myfont2 = pygame.font.SysFont("monospace", 30)
        score_display = myfont.render(str(jeu.joueur1.score1), 1, (0,0,0))
        screen.blit(score_display, (400, 15))
        score_display2 = myfont.render(str(jeu.joueur2.score2), 1, (0,0,0))
        screen.blit(score_display2, (450, 15))
        score_display3 = myfont.render("Score: ", 1, (0,0,0))
        screen.blit(score_display3, (200, 10))
        score_display4 = myfont2.render("-", 1, (0,0,0))
        screen.blit(score_display4, (430, 25))
    
        #Les actions à faire lors de l'attaque d'un des 2 joueurs
        #C'est la meme chose que pour la version terminale avec moins de code 
        if (jeu.joueur2.rect.x - jeu.joueur1.rect.x) == jeu.attaque_range and (jeu.joueur1.mode_attaque == 1) and (jeu.joueur2.mode_attaque == 1):
            jeu.restart()
        if (jeu.joueur2.rect.x - jeu.joueur1.rect.x) == jeu.attaque_range and (jeu.joueur1.mode_defense == 1) and (jeu.joueur2.mode_attaque == 1):
            jeu.joueur1.mode_defense = 0
            jeu.joueur2.mode_attaque = 0
            jeu.joueur1.image = pygame.image.load('image/leftImgparry.png')
            screen.blit(jeu.joueur1.image, jeu.joueur1.rect)
            jeu.joueur2.image = pygame.image.load('image/rightImgparry.png')
            screen.blit(jeu.joueur2.image, jeu.joueur2.rect)
        if (jeu.joueur2.rect.x - jeu.joueur1.rect.x) == jeu.attaque_range and (jeu.joueur1.mode_attaque == 1) and (jeu.joueur2.mode_defense == 1):
            jeu.joueur1.mode_attaque = 0
            jeu.joueur2.mode_defense = 0
            jeu.joueur1.image = pygame.image.load('image/leftImgparry.png')
            screen.blit(jeu.joueur1.image, jeu.joueur1.rect)
            jeu.joueur2.image = pygame.image.load('image/rightImgparry.png')
            screen.blit(jeu.joueur2.image, jeu.joueur2.rect)
        else:
            if jeu.joueur1.mode_attaque == 0 and jeu.joueur1.mode_defense == 0:
                jeu.joueur1.image = pygame.image.load('image/leftImgparry.png')
                screen.blit(jeu.joueur1.image, jeu.joueur1.rect)
            
            if jeu.joueur1.mode_attaque == 1:
                jeu.joueur1.image = pygame.image.load('image/leftImgattack.png')
                screen.blit(jeu.joueur1.image, jeu.joueur1.rect)
                if (jeu.joueur2.rect.x - jeu.joueur1.rect.x ) == jeu.attaque_range:
                    jeu.joueur1.score1 += 1
                    jeu.restart()
                jeu.joueur1.mode_attaque = 0
    
            if jeu.joueur2.mode_attaque == 0 and jeu.joueur2.mode_defense == 0:
                jeu.joueur2.image = pygame.image.load('image/rightImgparry.png')
                screen.blit(jeu.joueur2.image, jeu.joueur2.rect)
            
            if jeu.joueur2.mode_attaque == 1:
                jeu.joueur2.image = pygame.image.load('image/rightImgattack.png')
                screen.blit(jeu.joueur2.image, jeu.joueur2.rect)
                if (jeu.joueur2.rect.x - jeu.joueur1.rect.x ) == jeu.attaque_range:
                    jeu.joueur2.score2 += 1
                    jeu.restart()
                jeu.joueur2.mode_attaque = 0  
            
            if jeu.joueur1.mode_defense == 1:
                jeu.joueur1.image = pygame.image.load('image/leftImg.png')
                screen.blit(jeu.joueur1.image, jeu.joueur1.rect)
                jeu.joueur1.mode_defense = 0 
            
            if jeu.joueur2.mode_defense == 1:
                jeu.joueur2.image = pygame.image.load('image/rightImg.png')
                screen.blit(jeu.joueur2.image, jeu.joueur2.rect)
                jeu.joueur2.mode_defense = 0 
        #Saut pour le joueur 1    
        if jeu.joueur1.saut1 == 1:
            jeu.joueur1.jump_right()   
        if jeu.joueur1.saut2 == 1:
            jeu.joueur1.jump_left() 
        #Saut pour le joueur 2  
        if jeu.joueur2.saut1 == 1:
            jeu.joueur2.jump_right()
        if jeu.joueur2.saut2 == 1:
            jeu.joueur2.jump_left()
    
        #avancer joueur 1
        if jeu.presser.get(pygame.K_d) and jeu.joueur1.rect.x < (jeu.joueur2.rect.x - 90): 
            jeu.joueur1.move_right()
        #reculer joueur 1
        if jeu.presser.get(pygame.K_q) and jeu.joueur1.rect.x >= 0:
            jeu.joueur1.move_left()
        #reculer joueur 2
        if jeu.presser.get(pygame.K_RIGHT) and jeu.joueur2.rect.x + jeu.joueur2.rect.width < screen.get_width():
            jeu.joueur2.move_right()
        #avancer joueur 2
        if jeu.presser.get(pygame.K_LEFT) and jeu.joueur2.rect.x > (jeu.joueur1.rect.x + 90):
            jeu.joueur2.move_left()
        #sauter à droite le joueur 1
        if jeu.presser.get(pygame.K_e) and jeu.joueur1.rect.x < (jeu.joueur2.rect.x - 90):
            jeu.joueur1.saut1 = True
        #sauter à gauche et en reculant le joueur 1
        if jeu.presser.get(pygame.K_a) and jeu.joueur1.rect.x >= 20:
            jeu.joueur1.saut2 = True
        #sauter à droite le joueur 2
        if jeu.presser.get(pygame.K_m) and jeu.joueur2.rect.x + jeu.joueur2.rect.width < screen.get_width():
            jeu.joueur2.saut1 = True
        #sauter à gauche et en reculant le joueur 1
        if jeu.presser.get(pygame.K_l) and jeu.joueur2.rect.x > (jeu.joueur1.rect.x + 90):
            jeu.joueur2.saut2 = True   
        #le joueur 2 est en mode attaque     
        if jeu.presser.get(pygame.K_o):
            jeu.joueur2.mode_attaque = 1
        #le joueur 1 est en mode attaque 
        if jeu.presser.get(pygame.K_z):
            jeu.joueur1.mode_attaque = 1
        #le joueur 1 est en mode defense
        if jeu.presser.get(pygame.K_s):
            jeu.joueur1.mode_defense = 1
        #le joueur 2 est en mode defense
        if jeu.presser.get(pygame.K_p):
            jeu.joueur2.mode_defense = 1  
        #mettre le jeu en pause et ouvrir le menu
        if jeu.presser.get(pygame.K_SPACE):
            jeu.pause = True
            mixer.music.load("zelda-main-theme-song.mp3")
            mixer.music.play(-1)
         
    pygame.display.flip()
    
    #Gerer les evenement des joueurs et les insérer dans des dictionnaires
    #pour pouvoir les utiliser en meme temps 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu.run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            jeu.presser[event.key] = True
        elif event.type == pygame.KEYUP:
            jeu.presser[event.key] = False