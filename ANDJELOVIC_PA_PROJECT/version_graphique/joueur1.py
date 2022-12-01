import pygame

class Joueur1(pygame.sprite.Sprite):
    #On reprensente le joueur avec sa propre image 
    def __init__(self):
        super().__init__()
        self.mouvement_speed = 2
        self.attaque_speed = 10
        self.image = pygame.image.load('image/leftImgparry.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.saut1 = False
        self.saut2 = False
        self.gravite = 1
        self.taille_saut = 15
        self.speed = self.taille_saut
        self.mode_attaque = 0
        self.mode_defense = 0
        self.score1 = 0
        
    #Fonction qui permet de déplacer le joueur    
    def move_right(self):
        self.rect.x += self.mouvement_speed
        
    #Fonction qui permet de reculer le joueur    
    def move_left(self):
        self.rect.x -= self.mouvement_speed
        
    #Les fonctions du saut sont les memes le deplacement les differencie
    #Les fonctions saut fonctionne de cette manière tout d'abord on degremente 
    #la coordonnées y qui nous feras monter ensuite quand on a atteint l'apaugé
    #c'est à dire -la taille du saut on fait retomber le joueur entre temps 
    #on avance à gauche ou à droite
    #Fonction qui permet de sauter à droite 
    def jump_right(self):
        self.rect.y -= self.speed
        self.speed -= self.gravite
        self.move_right()
        if  self.speed < -self.taille_saut:
            self.saut1 = False
            self.speed = self.taille_saut
            
    #Fonction qui permet de sauter à gauche 
    def jump_left(self):
        self.rect.y -= self.speed
        self.speed -= self.gravite
        self.move_left()
        if  self.speed < -self.taille_saut:
            self.saut2 = False
            self.speed = self.taille_saut

        
        
        