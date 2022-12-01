#Cette classe a été repris et fais grace à une vidéo sur Youtube 
#Elle implemente des boutons et l'interaction avec les boutons

import pygame

class Boutton():
	def __init__(self, x, y, image, echelle):
		longueur = image.get_width()
		hauteur = image.get_height()
		self.image = pygame.transform.scale(image, (int(longueur * echelle), int(hauteur * echelle)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.cliquer = False
  
	#Cette fonction fais 2 chose, premier chose elle dessine le boutton sur l'ecran 
 	#deuxiement elle cherche la position de la souris la compare si elle cohenside avec le boutton en question
	#et ensuite regarde si l'utilisateur clique dessus et retourne vrai ou faux
	def draw(self, surface):
		action = False
		#permet d'avoir la position de la souris
		pos = pygame.mouse.get_pos()

		#cherche si la souris est pardessus le bouton et si l'utilisateur clique dessus 
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.cliquer == False:
				self.cliquer = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.cliquer = False

		#dessine un boutton sur l'ecran
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action