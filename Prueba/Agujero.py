import pygame
from Funciones import rotarCentro, sumarAngulo
from Pantalla import Pantalla

class Agujero:
	def imprimir(self, camara):
		camara.display.blit(rotarCentro(self.imagen, self.angulo), (-camara.getX()+self.origenX,camara.getY()-self.origenY))
		self.angulo = sumarAngulo(self.angulo, self.velocidad)
	def __init__(self, directorio, origenX, origenY, velocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.origenX = origenX
		self.origenY = origenY
		self.angulo = 0
		self.velocidad = velocidad