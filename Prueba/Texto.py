import pygame
from pygame.locals import * 
class Texto:
	def setTexto(self, texto):
		self.surTexto = self.fuente.render(texto, True, self.color)
		
	def imprimir(self, destino, x, y):
		destino.display.blit(self.surTexto,(x, y))
	
	def __init__(self, path_fuente, fsize, color = pygame.Color(0,0,255)):
		self.fuente = pygame.font.Font("Recursos/arial.ttf", fsize)
		self.color = color
