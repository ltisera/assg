import math, pygame
from Pantalla import Pantalla

class Laser:		
	def mover(self, X, Y):
		self.X += math.cos(math.radians(self.angulo))*self.velocidad - X
		self.Y -= math.sin(math.radians(self.angulo))*self.velocidad + Y
	def imprimir(self, X, Y, camara):
		self.mover(X, Y)
		if (self.X >= 0 and self.X <= 650) and (self.Y >= 0 and self.Y <= 475):
			camara.display.blit(pygame.transform.rotate(self.imagen, self.angulo), (self.X,self.Y))
		else:
			self.laserLibre = True
	def setLaser(self, camara, velocidad, angulo, libre):
		self.angulo = angulo
		self.velocidad = velocidad
		self.X = camara.getCentroX()
		self.Y = camara.getCentroY()
		self.laserLibre = libre
	def __init__(self, directorio, camara, velocidad, angulo, libre):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.angulo = angulo
		self.velocidad = velocidad
		self.X = camara.getCentroX()
		self.Y = camara.getCentroY()
		self.laserLibre = libre