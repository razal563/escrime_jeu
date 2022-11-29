#Cette classe a été trouvé sur github elle permet de créer des boutons et l'interraction avec celle-ci
import pygame

class Boutton():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
  
	#Cette fonction fais 2 chose, premier chose elle dessine le boutton sur l'ecran 
 	#deuxiement elle cherche la position de la souris la compare si elle cohenside avec le boutton en question
	#et ensuite regarde si l'utilisateur clique dessus et retourne vrai ou faux
	def draw(self, surface):
		action = False
		#permet d'avoir la position de la souris
		pos = pygame.mouse.get_pos()

		#cherche si la souris est pardessus le bouton et si l'utilisateur clique dessus 
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#dessine un boutton sur l'ecran
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action