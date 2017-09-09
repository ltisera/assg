import pygame

class Pantalla:
	def getCentro(self):
		return self.centro
		
	def getCentroX(self):
		return self.centro[0]
		
	def getCentroY(self):
		return self.centro[1]
			
	def __init__(self):
		self.display = pygame.display.set_mode((800,600))
		pygame.display.set_caption("ASSG")
		self.fondo1 = pygame.image.load("Recursos/1.png").convert_alpha()
		self.fondo2 = pygame.image.load("Recursos/2.png").convert_alpha()
		self.centro = (325, 237.5)
		