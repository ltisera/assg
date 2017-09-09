import pygame, math
from Funciones import rotarCentro, sumarAngulo
from Pantalla import Pantalla

class Nave:
	def sumarAngulo(self, sumAngulo):
		self.angulo = sumarAngulo(self.angulo, sumAngulo)
		self.mover()
		
	def sumarVelocidad(self, sumar):
		self.velocidad = self.velocidad + sumar
		if self.velocidad <= (self.minVelocidad):
			self.velocidad = self.minVelocidad
		elif self.velocidad >= (self.maxVelocidad):
			self.velocidad = self.maxVelocidad
		self.mover()
		
	def boom(self):
		self.colision = True
		
	def mover(self):
		self.X = math.cos(math.radians(self.angulo))*self.velocidad
		self.Y = -math.sin(math.radians(self.angulo))*self.velocidad
		
	def imprimir(self, camara):
		camara.display.blit(rotarCentro(self.imagen, self.angulo), (camara.getCentroX()-57, camara.getCentroY()-57))
		if self.colision:
			camara.display.blit(self.imagenColision, (camara.getCentroX()-25, camara.getCentroY()-25))
			self.colision = False
		
	def __init__(self, directorio,directorio2, anguloOrigen, velocidad, minVelocidad, maxVelocidad, origen):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.imagenColision = pygame.image.load(directorio2).convert_alpha()
		self.colision = False
		self.imagen = pygame.transform.rotate(self.imagen, anguloOrigen)
		self.X = origen[0]
		self.Y = origen[1]
		self.maxVelocidad = maxVelocidad
		self.minVelocidad = minVelocidad
		self.angulo = 0
		self.velocidad = 0
		self.sumarVelocidad(velocidad)