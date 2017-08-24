import pygame

class Pantalla:
	def imprimir(self):
		pantalla = Pantalla()
		pantalla.display.blit(self.fondo1, (650,0))
		pantalla.display.blit(self.fondo2, (0,475))
	def mover(self, X, Y):
		self.X += X
		self.Y += Y
	def __init__(self):
		self.display = pygame.display.set_mode((800,600))
		pygame.display.set_caption("ASSG")
		self.X = 0
		self.Y = 0
		self.fondo1 = pygame.image.load("Recursos/1.png").convert_alpha()
		self.fondo2 = pygame.image.load("Recursos/2.png").convert_alpha()
		self.centroX = 325
		self.centroY = 237.5