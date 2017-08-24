import pygame, math

class Nave:
	def sumarAngulo(self, sumarAngulo):
		self.angulo += sumarAngulo
		if self.angulo >= 360:
			self.angulo -= 360
		elif self.angulo < 0:
			self.angulo += 360
		self.mover()
	def sumarVelocidad(self, sumar):
		self.velocidad = self.velocidad + sumar
		if self.velocidad <= (self.minVelocidad):
			self.velocidad = self.minVelocidad
		elif self.velocidad >= (self.maxVelocidad):
			self.velocidad = self.maxVelocidad
		self.mover()
	def mover(self):
		self.X = math.cos(math.radians(self.angulo))*self.velocidad
		self.Y = math.sin(math.radians(self.angulo))*self.velocidad
	def imprimir(self, centroX, centroY, pantalla):
		pantalla.display.blit(pygame.transform.rotate(self.imagen, self.angulo), (centroX-38,centroY-27))
	def __init__(self, directorio, anguloOrigen, velocidad, minVelocidad, maxVelocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.imagen = pygame.transform.rotate(self.imagen, anguloOrigen)
		self.X = 0
		self.Y = 0
		self.maxVelocidad = maxVelocidad
		self.minVelocidad = minVelocidad
		self.angulo = 0
		self.velocidad = 0
		self.sumarVelocidad(velocidad)