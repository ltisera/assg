import pygame, math
from Pantalla import Pantalla

class Enemigo:
	def mover(self, X, Y, camara):
		self.X -= X
		self.Y += Y
		distancia = math.sqrt(math.pow((self.X-camara.getCentroX()-20),2)+math.pow((self.Y-camara.getCentroY()-20),2))
		#Si el enemigo esta lejos, se acerca a la nave
		if distancia > 175:							
			if self.X < camara.getCentroX()-20:
				self.X += self.velocidad
			elif self.X > camara.getCentroX()-20:
				self.X -= self.velocidad
			if self.Y < camara.getCentroY()-20:
				self.Y += self.velocidad
			elif self.Y > camara.getCentroY()-20:
				self.Y -= self.velocidad
		#Y si esta demasiado cerca se aleja
		else:
			if self.X < camara.getCentroX()-20:
				self.X -= self.velocidad
			elif self.X > camara.getCentroX()-20:
				self.X += self.velocidad
			if self.Y < camara.getCentroY()-20:
				self.Y -= self.velocidad
			elif self.Y > camara.getCentroY()-20:
				self.Y += self.velocidad
			
	def imprimir(self, X, Y, camara):
		self.mover(X, Y, camara)
		camara.display.blit(self.imagen, (self.X,self.Y))
	def __init__(self, directorio, X, Y, velocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.X = X
		self.Y = Y
		self.velocidad = velocidad