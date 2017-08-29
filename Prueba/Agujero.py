import pygame, random
from Funciones import rotarCentro, sumarAngulo, lugarLibre
from Pantalla import Pantalla

class Agujero:
	def getCentro(self):
		return self.centro
	def getCentroX(self):
		return self.centro[0]
	def getCentroY(self):
		return self.centro[1]
	def imprimir(self, camara):
		self.angulo = sumarAngulo(self.angulo, self.velocidad)
		if (self.getCentroX()-camara.getX() >= -400 and self.getCentroX()-camara.getX() <= 1400) and (self.getCentroY()-camara.getY() >= -400 and self.getCentroY()-camara.getY() <= 1400):
			camara.display.blit(rotarCentro(self.imagen, self.angulo), (self.origenX-camara.getX(),self.origenY-camara.getY()))
	def __init__(self, directorio, velocidad, lobjeto, AREA_MAXIMA, DISTANCIA_MINIMA):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.velocidad = velocidad
		self.angulo = 0
		asignado = False
		while not asignado:
			self.origenX = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.origenY = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.centro = ((self.imagen.get_width()/2) + self.origenX, (self.imagen.get_height()/2) + self.origenY)
			asignado = lugarLibre(self, lobjeto, DISTANCIA_MINIMA)
		
		