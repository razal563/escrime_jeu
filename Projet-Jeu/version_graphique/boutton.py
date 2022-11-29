#Cette classe permet d'implémenter des boutons avec leur position et l'image qui leur appartient
import pygame

class Boutton():
	def __init__(self, x, y, image, echelle):
		largeur = image.get_width()
		hauteur = image.get_height()
		self.image = pygame.transform.scale(image, (int(largeur * echelle), int(hauteur * echelle)))
		self.rect = self.image.get_rect()
		self.rect.haut_gauche = (x, y)
		self.cliquer_source = False
  
	#Cette fonction fais 2 chose, premier chose elle dessine le boutton sur l'ecran 
 	#deuxiement elle cherche la position de la souris la compare si elle cohenside avec le boutton en question
	#et ensuite regarde si l'utilisateur clique dessus et retourne vrai ou faux
	def draw(self, surface):
		action = False
		#permet d'avoir la position de la souris
		pos = pygame.mouse.get_pos()

		#cherche si la souris est pardessus le bouton et si l'utilisateur clique dessus 
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.cliquer_source == False:
				self.cliquer_source = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.cliquer_source = False

		#dessine un boutton sur l'ecran
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
