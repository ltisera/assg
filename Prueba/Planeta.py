import pygame, random
from Funciones import distancia, lugarLibre
from Pantalla import Pantalla

class Planeta:
	def getCentro(self):
		return self.centro
	def getCentroX(self):
		return self.centro[0]
	def getCentroY(self):
		return self.centro[1]
	def setX(self, x):
		self.origenX = x
	def setY(self, y):
		self.origenY = Y
	def imprimir(self, camara):
		if (self.getCentroX()-camara.getX() >= -400 and self.getCentroX()-camara.getX() <= 1400) and (self.getCentroY()-camara.getY() >= -400 and self.getCentroY()-camara.getY() <= 1400):
			camara.display.blit(self.imagen, (self.origenX-camara.getX(),self.origenY-camara.getY()))	
	def __init__(self, directorio, lplaneta, AREA_MAXIMA, DISTANCIA_MINIMA):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		asignado = False
		while not asignado:
			self.origenX = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.origenY = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.centro = ((self.imagen.get_width()/2) + self.origenX, (self.imagen.get_height()/2) + self.origenY)
			asignado = lugarLibre(self, lplaneta, DISTANCIA_MINIMA)