import pygame
from Pantalla import Pantalla

class Enemigo:
	def mover(self, X, Y, camara):
		self.X -= X
		self.Y += Y
		if self.X < camara.getCentroX()-20:
			self.X += self.velocidad
		elif self.X > camara.getCentroX()-20:
			self.X -= self.velocidad
		if self.Y < camara.getCentroY()-20:
			self.Y += self.velocidad
		elif self.Y > camara.getCentroY()-20:
			self.Y -= self.velocidad
	def imprimir(self, X, Y, camara):
		self.mover(X, Y, camara)
		camara.display.blit(self.imagen, (self.X,self.Y))
	def __init__(self, directorio, X, Y, velocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.X = X
		self.Y = Y
		self.velocidad = velocidad