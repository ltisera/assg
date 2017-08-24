import math, pygame
from Pantalla import Pantalla

class Laser:
	def mover(self):
		self.X -= math.cos(math.radians(self.angulo))*self.velocidad
		self.Y += math.sin(math.radians(self.angulo))*self.velocidad
	def imprimir(self, camara):
		self.mover()
		if self.contador <= 50:
			camara.display.blit(pygame.transform.rotate(self.imagen, self.angulo), (self.X,self.Y))
			self.contador += 1
			self.velocidad -= 0.5
			return True
		else:
			return False
	def __init__(self, directorio, camara, velocidad, angulo):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.angulo = angulo
		self.velocidad = velocidad
		self.X = camara.getCentroX()
		self.Y = camara.getCentroY()
		self.contador = 0